
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
        replyButtons.forEach(btn => {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                const username = this.getAttribute('data-username');
                const commentId = this.getAttribute('data-comment-id');

                // Set parent ID
                parentIdInput.value = commentId;

                // Show replying UI
                replyUsernameSpan.textContent = `@${username}`;
                replyingToLabel.classList.remove('d-none');

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
                parentIdInput.value = '';
                replyingToLabel.classList.add('d-none');
                commentInput.value = '';
                commentInput.placeholder = 'leave a note...';
            });
        }
    }
});
