// .dropdown-content 内のリンクにホバーされたとき
const dropdownLinks = document.querySelectorAll(
  "#main-nav .dropdown-content a"
);

dropdownLinks.forEach((link) => {
  link.addEventListener("mouseenter", function () {
    // hover時に親要素の .dropbtn を見つけて色を変更
    const dropbtn = this.closest(".dropdown").querySelector(".dropbtn");
    dropbtn.style.color = "rgba(255, 0, 0, 1)";
  });

  link.addEventListener("mouseleave", function () {
    // hoverが外れたら元の色に戻す
    const dropbtn = this.closest(".dropdown").querySelector(".dropbtn");
    dropbtn.style.color = ""; // 初期スタイルに戻す
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const footer = document.getElementById("footer");
  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        footer.classList.add("show");
      }
    },
    { threshold: 0.1 }
  );
  observer.observe(footer);
});
