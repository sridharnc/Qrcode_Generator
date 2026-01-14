<link href="/static/css/style.css"/>
<script>
// Mobile Menu Toggle
const mobileMenu = document.getElementById("mobile-menu");
const navLinks = document.querySelector(".nav-links");

mobileMenu.addEventListener("click", () => {
  navLinks.style.display =
    navLinks.style.display === "flex" ? "none" : "flex";
});
</script>