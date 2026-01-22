document.addEventListener("DOMContentLoaded", function () {
    const navWrap = document.querySelector(".wy-nav-content-wrap");
    const navSide = document.querySelector(".wy-nav-side");
  
    if (!navWrap || !navSide) return;
  
    const toggleBtn = document.createElement("div");
    toggleBtn.innerHTML = "☰";
    toggleBtn.classList.add("toggle-sidebar-btn");
  
    document.body.appendChild(toggleBtn);
  
    toggleBtn.addEventListener("click", function () {
      navWrap.classList.toggle("collapsed");
      navSide.classList.toggle("collapsed");
    });
  });
  