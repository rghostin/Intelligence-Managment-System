function create_intel_base(api_endpoint, data) {
    console.log(data);
    console.log(data.title);
    return $.ajax({
        type: "POST",
        url: api_endpoint,
        data: data,
        success: function(response) {
        }
    });
}


function create_intel(api_endpoint_intel, api_endpoint_intelfiles, csrf_token, form_data_base) {
    let xhr_base = create_intel_base(api_endpoint_intel, form_data_base);
    xhr_base.fail( () => {console.log("Error: unable to create base intel");});
    xhr_base.done( function (data_intel_base) {
        let intel_id = data_intel_base.id;
        console.log("Base intel created successfully id=" + data_intel_base.id);

        let failed=false;
        let files = $('#file')[0].files;
        Array.from(files).forEach( function (file) {
            let xhr_file = upload_file(api_endpoint_intelfiles, csrf_token, intel_id, file);
            xhr_file.fail( () => {failed=true; console.log("Failed to upload "+f.name);} )
            xhr_file.done(data_intel_file => {
                console.log("Uploaded file " + file.name + "id=" + data_intel_file.id + " to intel_id=" + intel_id);
            });
        });

        // todo when all promises done
        // if (failed) {
        //     console.log("Intel created successful");
        // } else {
        //     console.log("Error : Failure");
        // }

    });

}

function upload_selected_files(api_endpoint, csrf_token, intel_id) {
    var files = $('#file')[0].files;
    console.log(files);
    Array.from(files).forEach(file => { upload_file(api_endpoint, csrf_token, intel_id, file); });
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
      success: function(response){
         console.log("-Uploaded file " + file.name + " to " + intel_id);
      },
   });

}