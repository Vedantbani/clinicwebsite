// Automatically close the mobile navbar menu when a link is clicked
document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link, .navbar-collapse .btn");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            // Check if the mobile menu is currently expanded/open
            if (navbarCollapse.classList.contains("show")) {
                // Use Bootstrap's built-in collapse method to toggle/hide it
                const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
                if (bsCollapse) {
                    bsCollapse.hide();
                } else {
                    // Fallback initialization if instance isn't fetched yet
                    new bootstrap.Collapse(navbarCollapse).hide();
                }
            }
        });
    });
});