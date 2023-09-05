// Function to show a confirmation dialog on logout
function confirmLogout() {
    if (confirm("Are you sure you want to log out?")) {
        // Redirect to the logout route when the user confirms
        window.location.href = "{{ url_for('logout') }}";
    }
}

// Add event listeners to elements with specific IDs or classes
document.addEventListener("DOMContentLoaded", function () {
    // Example: Add a click event listener to a button with the "logout-button" ID
    const logoutButton = document.getElementById("logout-button");
    if (logoutButton) {
        logoutButton.addEventListener("click", confirmLogout);
    }

    // You can add more event listeners and functionality as needed
});
