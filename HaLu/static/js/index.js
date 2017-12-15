window.onload = function() {
    var filenames = new Array('bk_img001.jpg', 'bk_img002.jpg', 'bk_img003.jpg', 'bk_img004.jpg');
    count = -1; //*2

    setInterval(function changeBgImg() {
        count++; //*3
        if (count == filenames.length) count = 0;
        //画像出力

        var elm = document.getElementById('wrapper');
        elm.style.backgroundImage = 'url(/static/img/bg/' + filenames[count] + ')';
    }, 7000);
}