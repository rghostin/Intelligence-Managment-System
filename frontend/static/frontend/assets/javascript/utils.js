function debounce(duration, fn) {
    // add delay before tiggering event
    // duration: ms
    var timer;
    return function() {
        clearTimeout(timer);
        timer = setTimeout(fn, duration)
    }
}


function display_notification(notification_type, msg) {
    switch (notification_type) {
        case "success":
           One.helpers('notify', {type: 'success', icon: 'fa fa-check mr-1', message: msg});
           break;
        case "error":
           One.helpers('notify', {type: 'danger', icon: 'fa fa-times mr-1', message: msg});
            break;
        default:
            console.error("Unknown notification type "+notification_type);
    }
}
