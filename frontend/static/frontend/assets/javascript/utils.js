function debounce(duration, fn) {
    // add delay before tiggering event
    // duration: ms
    var timer;
    return function() {
        clearTimeout(timer);
        timer = setTimeout(fn, duration)
    }
}


function capFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}