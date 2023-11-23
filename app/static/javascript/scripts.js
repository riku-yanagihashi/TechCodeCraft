document.addEventListener('DOMContentLoaded', function() {
	document.querySelector('a[href="#top"]').addEventListener('click', function(e) {
		e.preventDefault();

		// スムーズなスクロールのためのアニメーション
		document.querySelector('html, body').animate({
			scrollTop: 0
		}, 800); // アニメーションの速さ（ミリ秒単位）

	});
});
