

document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript loaded and ready!");
    
    // Add your JavaScript functionality here
    // Example: Alert on form submission
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function() {
            alert("Form is being submitted!");
        });
    });
});
