function create_intel_base(api_endpoint, data) {
    return $.ajax({
        type: "POST",
        url: api_endpoint,
        data: data,
        success: function(response) {
        }
    });
}


function upload_file(api_endpoint, csrf_token, intel_id, file) {
    var fd = new FormData();
    fd.append("csrfmiddlewaretoken", csrf_token);
    fd.append("intel", intel_id);
    fd.append('file', file);

   return $.ajax({
      url: api_endpoint,
      type: 'post',
      data: fd,
      contentType: false,
      processData: false,
      success: function(response){},
   });
}

function getSelectedFiles() {
    return $('#id_input_files')[0].files;
}


function display_status(failed) {
    if (failed) {
        console.log("Error : Failure creating intel");
        display_notification("error", "Failure creating intel")
    } else {
        console.log("Intel created successfully");
        display_notification("success", "Intel created successfully !")
    }
}

function create_intel(api_endpoint_intel, api_endpoint_intelfiles, csrf_token, form_data_base) {
    var failed = false;
    let xhr_base = create_intel_base(api_endpoint_intel, form_data_base);
    let deferreds = [];
    xhr_base.fail( function () {
        failed=true;
        console.log("Error: unable to create base intel");
        display_status(failed);
    });
    xhr_base.done( function (data_intel_base) {
            let intel_id = data_intel_base.id;
            console.log("Base intel created successfully id=" + data_intel_base.id);

            let files = getSelectedFiles();
            Array.from(files).forEach(function (file) {
                let xhr_file = upload_file(api_endpoint_intelfiles, csrf_token, intel_id, file);
                xhr_file.fail(() => {
                    // todo rollback
                    failed = true;
                    console.log("Failed to upload " + f.name);
                });
                xhr_file.done(data_intel_file => {
                    console.log("Uploaded file " + file.name + " id=" + data_intel_file.id + " to intel_id=" + intel_id);
                });
                deferreds.push(xhr_file);
            });

            $.when.apply($, deferreds).then(function (){
                display_status(failed);
            });
        }
    );

}

