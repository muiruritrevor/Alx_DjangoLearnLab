from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework
from rest_framework.response import Response
from notifications.models import Notification


# Create Views for CRUD Operations

# Custom permission to only allow authors of an object to edit or delete it.
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of the post/comment
        return obj.author == request.user


# Post view
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        post.save()
        

# Comment view
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        post = comment.post

        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb= f'commented on your post {post.title}',
                target = post
            )



# A Feed view to display posts of following users 
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the list of all users the current user is following
        following_users = self.request.user.following.all()

        # Retrieve post from the users the current user is following, ordering by most recent date created
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


# Defining a view for liking posts
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            recipient = post.author,
            actor = request.user,
            verb = f'liked your post {post.title}',
            target = post
        )
        return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)


# A view to unlike a post if it exist or not already liked
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'message': "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate
# from .serializers import RegisterSerializer
# from rest_framework import generics, permissions
# from .serializers import UserProfileSerializer
# from rest_framework import status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import CustomUser
# from rest_framework import viewsets


# class UserViewSet(generics.GenericAPIView):
#     queryset = CustomUser.objects.all()
#     permission_classes = [IsAuthenticated]

#     @action(detail=True, methods=['post'])
#     def follow(self, request, pk=None):
#         user = self.get_object()
#         request.user.following.add(user)
#         return Response({'status': 'following'}, status=status.HTTP_200_OK)

#     @action(detail=True, methods=['post'])
#     def unfollow(self, request, pk=None):
#         user = self.get_object()
#         request.user.following.remove(user)
#         return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)


# class UserProfileView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         # Returns the authenticated user's profile
#         return self.request.user

#     def get(self, request, *args, **kwargs):
#         # Return user's profile information
#         serializer = self.get_serializer(request.user)
#         return Response(serializer.data)

#     def put(self, request, *args, **kwargs):
#         # Update the authenticated user's profile
#         user = self.get_object()
#         serializer = self.get_serializer(user, data=request.data, partial=True)  # partial=True allows partial updates
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=status.HTTP_200_OK)
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)