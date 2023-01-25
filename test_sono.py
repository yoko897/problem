$(window).on('load orientationchange resize', function(){
    if (Math.abs(window.orientation) === 90) {
        Screen.lockOrientation('landscape');
    } else {
        // 縦向きになったときの処理
    }
});