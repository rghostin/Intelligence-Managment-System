function add_to_files_list(file_url) {
    let filename = file_url.substring(file_url.lastIndexOf('/')+1);
    let files_count = get_files_count();
    if (files_count === 0) {
        $("#id_files_ul").html('<ul id="id_files_ul"></ul>')
    }
    let entry = `<li><a href="${file_url}" target="_blank">${filename}</a></li>`;
    $("#id_files_ul").append(entry);
    set_files_count(files_count+1)
}

function get_files_count() {
    return parseInt($("#id_file_count").text());
}

function set_files_count(n) {
    $("#id_file_count").html(n);
}

function set_drag_display(setOn) {
    if (setOn) {
        $(".dzone").addClass("in")
    } else {
        $(".dzone").removeClass("in")
    }
}


$( document ).ready(function() {

      $(".js-upload-photos").click(function () {
        $("#fileupload").click();
      });

      // init file upload
    $("#fileupload").fileupload({
        dataType: 'json',
        dropZone: $(".dzone"),
        sequentialUploads: true,  /* 1. SEND THE FILES ONE BY ONE */
        start: function (e) {  /* 2. WHEN THE UPLOADING PROCESS STARTS, SHOW THE MODAL */
          $("#modal-progress").modal("show");
        },
        stop: function (e) {  /* 3. WHEN THE UPLOADING PROCESS FINALIZE, HIDE THE MODAL */
          $("#modal-progress").modal("hide");

        },
        progressall: function (e, data) {  /* 4. UPDATE THE PROGRESS BAR */
          var progress = parseInt(data.loaded / data.total * 100, 10);
          var strProgress = progress + "%";
          $(".progress-bar").css({"width": strProgress});
          $(".progress-bar").text(strProgress);
        },
        done: function (e, data) {
            console.log(data);
            add_to_files_list(data.result.file);
            set_drag_display(false);
        },
        error: function (e, data) {
            display_notification("error", "Unable to upload file");
        }
      });

});

$(".dzone").bind('dragover', function (e) {
set_drag_display(true);
});

$(".dzone").bind('dragleave', function (e) {
set_drag_display(false);
});


function delete_file(file_endpoint, file_id, csrftoken) {
    $.ajax({
        url: file_endpoint,
        type: "DELETE",
        // contentType: "application/json",
        // dataType: 'json',
        headers: {
            'X-CSRFTOKEN': csrftoken
        },
        beforeSend: function(jqXHR, settings) {console.log("before");},
        success: function(data){ console.log("success"); rm_file_from_list(file_id) },
        error: function () {
          display_notification("error", "Unable to load search results");
        }
    });
}

function rm_file_from_list(file_id) {
    let li_id = "#id_il_file_"+file_id;
    $(li_id).remove();
    set_files_count(get_files_count()-1);
}