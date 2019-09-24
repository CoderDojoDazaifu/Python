'use strict';

{
  // ボタン(Divタグ)
  const btn = document.getElementById('btn');

  btn.addEventListener('click', () => {
    const r = Math.random(); // 0以上、1未満の数値
    if (r < 0.2) {
      // 約20%の確率
      btn.textContent = '大吉♡';
    } else if (r < 0.4) {
      // 約20%の確率
      btn.textContent = '中吉♦';
    } else if (r < 0.6) {
      // 約20%の確率
      btn.textContent = '小吉♠';
    } else if (r < 0.8) {
      // 約20%の確率
      btn.textContent = '吉♣';
    } else if (r < 0.95) {
      // 約15%の確率
      btn.textContent = '末吉';
    } else {
      // 約5%の確率
      btn.textContent = '凶( ;∀;)';
    }
  });

  btn.addEventListener('mousedown', () => {
    // マウスがクリックされたら、cssのクラスを追加
    // ボタンが押されたように見せている
    btn.classList.add('pressed');
  });

  btn.addEventListener('mouseup', () => {
    // マウスのクリックが終わったら、cssのクラスを削除
    // ボタンが押されたように見せている
    btn.classList.remove('pressed');
  });
}
