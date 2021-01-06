function add_spinner_rotate() {
    var spinner_html = `
    <div style="display: none; position: fixed; top: 12%; right: 40px; z-index: 99999;" id="id_spinner_rotate">
        <div class="spinner-border text-success" role="status">
            <span class="sr-only">Loading...</span>
        </div>
    </div>`

    $("body").append(spinner_html);
}

function spinner_rotate_show() {
    if ($("#id_spinner_rotate").length === 0) {
        add_spinner_rotate();
    }
    $("#id_spinner_rotate").css('display','block');
}

function spinner_rotate_hide() {
    if ($("#id_spinner_rotate").length !== 0) {
        $("#id_spinner_rotate").css('display','none');
    }
}


function add_wheel_rotate() {
    console.log("adding w");
    var wheel_html = `
        <div style="display: none; position: fixed; top: 12%; right: 40px; z-index: 99999;" id="id_wheel_rotate">
            <i class="fa fa-2x fa-cog fa-spin"></i>
        </div>`
    $("body").append(wheel_html);
}

function wheel_rotate_show() {
    if ($("#id_wheel_rotate").length === 0) {
        add_wheel_rotate();
    }
    $("#id_wheel_rotate").css('display','block');
}

function wheel_rotate_hide() {
    if ($("#id_wheel_rotate").length !== 0) {
        $("#id_wheel_rotate").css('display','none');
    }
}