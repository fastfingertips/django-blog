
// Auto-dismiss alerts after 3 seconds
document.addEventListener("DOMContentLoaded", function () {
    // Alert Logic
    setTimeout(function () {
        let alerts = document.querySelectorAll(".alert");
        alerts.forEach(function (alert) {
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";
            setTimeout(function () {
                alert.remove();
            }, 500);
        });
    }, 3000);

    // Reply Button Logic (Delegated)
    document.body.addEventListener('click', function (e) {
        // Check for Reply Button click
        if (e.target.classList.contains('reply-btn')) {
            e.preventDefault();
            const btn = e.target;
            const targetSelector = btn.getAttribute('data-target');

            // Check if we are using the new inline system
            if (targetSelector) {
                const formContainer = document.querySelector(targetSelector);
                if (formContainer) {
                    // Toggle visibility
                    formContainer.classList.remove('d-none');
                    // Focus textarea
                    const textarea = formContainer.querySelector('textarea');
                    if (textarea) textarea.focus();
                }
            } else {
                // Legacy system (scroll to top) - keeping for fallback if needed, or if modifying older templates
                // But since we updated the template, this branch might not be hit for comments.
                // Leaving empty or minimal for now.
            }
        }

        // Check for Cancel Button click
        if (e.target.classList.contains('cancel-inline-reply-btn')) {
            e.preventDefault();
            const btn = e.target;
            const targetSelector = btn.getAttribute('data-target');
            const formContainer = document.querySelector(targetSelector);

            if (formContainer) {
                formContainer.classList.add('d-none');
                // Optional: clear textarea
                const textarea = formContainer.querySelector('textarea');
                if (textarea) textarea.value = '';
            }
        }

        // Toggle Replies Button
        const toggleBtn = e.target.closest('.toggle-replies-btn');
        if (toggleBtn) {
            e.preventDefault();
            const targetId = toggleBtn.getAttribute('data-bs-target');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                if (targetElement.classList.contains('d-none')) {
                    targetElement.classList.remove('d-none');
                    toggleBtn.innerHTML = toggleBtn.innerHTML.replace('▼', '▲').replace('show', 'hide');
                } else {
                    targetElement.classList.add('d-none');
                    toggleBtn.innerHTML = toggleBtn.innerHTML.replace('▲', '▼').replace('hide', 'show');
                }
            }
        }
    });
});
