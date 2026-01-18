
// Auto-dismiss alerts after 3 seconds
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let alerts = document.querySelectorAll(".alert");
        alerts.forEach(function (alert) {
            // Add fade-out effect
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";

            // Remove from DOM after fade-out
            setTimeout(function () {
                alert.remove();
            }, 500);
        });
    }, 3000); // Wait 3 seconds before starting fade-out
});
