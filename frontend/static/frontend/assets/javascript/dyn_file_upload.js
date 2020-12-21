function add_to_files_list(file_url) {
    let filename = file_url.substring(file_url.lastIndexOf('/')+1);
    let files_count = parseInt($("#id_file_count").text());
    if (files_count === 0) {
        $("#id_files_ul").html('<ul id="id_files_ul"></ul>')
    }
    let entry = `<li><a href="${file_url}" target="_blank">${filename}</a></li>`;
    $("#id_files_ul").append(entry);
    $("#id_file_count").html(files_count+1);
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
        }
      });

});

$(".dzone").bind('dragover', function (e) {
set_drag_display(true);
});

$(".dzone").bind('dragleave', function (e) {
set_drag_display(false);
});
