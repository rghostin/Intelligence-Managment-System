function add_to_files_list(file_result, file_size) {
    // todo fix - add_files_to_list: current is not consistent with template

    let file_id = file_result.id;
    let file_media_url = file_result.file;
    let creation_date = file_result.creation_date;
    let link = file_result.link;

    let filename = file_media_url.substring(file_media_url.lastIndexOf('/')+1);
    let files_count = get_files_count();

    var entry_link;
    if (link === "") {
        entry_link = `<a href="#" class="disabled">Link</a>`;
    } else {
        entry_link=`<a target="_blank" rel="noopener" href="${link}" data-toggle="tooltip" title="${link}">Link</a>`
    }

    let entry = `
            <tr id="id_il_file_${file_id}">
                <th class="text-center" scope="row">${files_count+1}</th>
                <td class="font-w600 font-size-sm">
                    <a href="${file_media_url}" target="_blank">${filename}</a>
                </td>
                <td>${entry_link}</td>
                <td>
                    ${file_size}
                </td>
                <td class="d-none d-sm-table-cell">
                    ${creation_date}
                </td>
                <td class="text-center">
                    <div class="btn-group">
                        <button type="button" class="btn btn-sm btn-light js-tooltip-enabled" data-toggle="tooltip" title="Delete file"
                        onclick="return false">
                            <i class="fa fa-fw fa-times"></i>
                        </button>
                    </div>
                </td>
            </tr>`;

    $("#id_tbody_files").append(entry);

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
            add_to_files_list(data.result, data.total);
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
        headers: {
            'X-CSRFTOKEN': csrftoken
        },
        success: function(data){
            rm_file_from_list(file_id);
            display_notification("warning", "File deleted");
        },
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