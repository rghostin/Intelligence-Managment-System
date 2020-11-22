function debounce(duration, fn) {
    // add delay before tiggering event
    // duration: ms
    var timer;
    return function() {
        clearTimeout(timer);
        timer = setTimeout(fn, duration)
    }
}