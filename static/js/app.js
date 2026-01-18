
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

    // Reply Button Logic
    const replyButtons = document.querySelectorAll('.reply-btn');
    const commentInput = document.querySelector('textarea[name="comment_content"]');
    const parentIdInput = document.querySelector('#parent_id');
    const replyingToLabel = document.querySelector('#replying-to');
    const replyUsernameSpan = document.querySelector('#reply-username');
    const cancelReplyBtn = document.querySelector('#cancel-reply');

    if (commentInput) {
        // Use event delegation for reply buttons too if they are dynamically added, 
        // but for now static list or page reload is fine. 
        // We'll keep existing logic for reply buttons but ensure it's safe.
        replyButtons.forEach(btn => {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                const username = this.getAttribute('data-username');
                const commentId = this.getAttribute('data-comment-id');

                // Set parent ID
                if (parentIdInput) parentIdInput.value = commentId;

                // Show replying UI
                if (replyUsernameSpan) replyUsernameSpan.textContent = `@${username}`;
                if (replyingToLabel) replyingToLabel.classList.remove('d-none');

                // Focus input
                commentInput.focus();
                commentInput.placeholder = `Reply to @${username}...`;

                // Scroll smoothly to input
                commentInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            });
        });

        if (cancelReplyBtn) {
            cancelReplyBtn.addEventListener('click', function () {
                // Clear state
                if (parentIdInput) parentIdInput.value = '';
                if (replyingToLabel) replyingToLabel.classList.add('d-none');
                commentInput.value = '';
                commentInput.placeholder = 'leave a note...';
            });
        }
    }

    // Toggle Replies Logic (Cleaned & Robust)
    document.body.addEventListener('click', function (e) {
        // Handle click on the button or any of its children
        const btn = e.target.closest('.toggle-replies-btn');

        if (btn) {
            e.preventDefault(); // Prevent default if it's a link or form submit
            const targetId = btn.getAttribute('data-bs-target'); // Keeping data-bs-target as matches template
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                if (targetElement.classList.contains('d-none')) {
                    // Show
                    targetElement.classList.remove('d-none');
                    // Change text: ▼ show -> ▲ hide
                    btn.innerHTML = btn.innerHTML.replace('▼', '▲').replace('show', 'hide');
                } else {
                    // Hide
                    targetElement.classList.add('d-none');
                    // Change text: ▲ hide -> ▼ show
                    btn.innerHTML = btn.innerHTML.replace('▲', '▼').replace('hide', 'show');
                }
            } else {
                console.warn('Target element not found:', targetId);
            }
        }
    });
});
