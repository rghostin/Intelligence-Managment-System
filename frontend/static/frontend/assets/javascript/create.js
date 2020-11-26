function create_intel(api_endpoint, data, csrf_token) {
    $.ajax({
        type: "POST",
        url: api_endpoint,
        data: data,
        success: function(data) {
           console.log(0);
           console.log(data);
           console.log(data.id);
        }
    });
}


function upload_selected_files(api_endpoint, intel_id) {
    var files = $('#file')[0].files;
    console.log(files);
    Array.from(files).forEach(file => { upload_file(api_endpoint, intel_id, file); });
}

function upload_file(api_endpoint, intel_id, file) {
    console.log("Uploading file " + file.name + " to " + intel_id);

    $("#id_intelfile_intel").val(intel_id);
    var form_base__upload = $("#id_form_files_upload")[0];

    console.log("form " + form_base__upload);
    var fd = new FormData(form_base__upload);
    fd.append('file', file);

   $.ajax({
      url: api_endpoint,
      type: 'post',
      data: fd,
      contentType: false,
      processData: false,
      success: function(response){
         console.log("Uploaded file " + file.name + " to " + intel_id);
      },
   });

}