function setParameter() {
    var obj = new Object();
    obj.category = getParameterCategory();
    obj.chapter = getParameterChapter();
    var jsonStr = JSON.stringify(obj);
    return serialize(jsonStr);

}

function getParameterCategory() {
    var paramsArray = [];
    for (var i = 0; i < document.search.category.length; i++) {
        if (document.search.category[i].checked) {
            paramsArray.push(document.search.category[i].value);
        }
    }
    return paramsArray;
};


function getParameterChapter() {
    var paramsArray = [];
    for (var i = 0; i < document.search.chapter.length; i++) {
        if (document.search.chapter[i].checked) {
            paramsArray.push(document.search.chapter[i].value);
        }
    }
    return paramsArray;
};

function lightTurn(on_or_off, var_id) {
    var val = var_id;
    var url_query = '/api/get_image/' + val + '/' + on_or_off;
    $.getJSON(url_query, function(data) {
        var img = $("#image_" + var_id).get(0);
        var id = data.id;
        var name = data.image;
        if (typeof name === "undefined") {
            var img_name = on_or_off ? 'no_image_white.png' : 'no_image_black.png'
            img.src = "/static/img/" + img_name;
        } else {
            img.src = "/static/" + name;
        }
    });
};

function switchlight() {
    var on_or_off = light_off ? 'on' : 'off'
    list.forEach(function(num) {
        lightTurn(on_or_off, num);
    });
    light_off = !(light_off);
    $('#main').toggleClass('darkness');
};