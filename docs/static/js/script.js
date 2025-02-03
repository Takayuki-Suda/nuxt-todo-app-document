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
