function copyToClipboard(button) {
  // ボタンの親要素の中から code 要素を取得
  const code = button.previousElementSibling.querySelector("code");
  const text = code.innerText;

  // クリップボードにコピー
  navigator.clipboard
    .writeText(text)
    .then(() => {
      // フィードバックメッセージの表示
      const feedback = button.nextElementSibling;
      feedback.classList.add("show");

      // 2秒後にフィードバックを非表示にする
      setTimeout(() => {
        feedback.classList.remove("show");
      }, 2000);
    })
    .catch((err) => {
      console.error("コピーに失敗しました: ", err);
    });
}
