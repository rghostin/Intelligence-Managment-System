function bookmark_add(api_endpoint, csrftoken, intel_id, link, filename) {
      $.ajax({
            url: api_endpoint,
            dataType: 'json',
            method: 'POST',
            headers: {
                'X-CSRFTOKEN': csrftoken
            },
            data: {"intel_id": intel_id, "link": link, "filename":filename},
            beforeSend: function() { wheel_rotate_show(); },
            complete: function () { wheel_rotate_hide(); },
            success: function(data){bookmark_added_success(data)},
            error: function () {
                display_notification("error", "Unable to save bookmark");
            }
        });
}

function bookmark_added_success(data) {
    add_to_files_list(data.file);
    display_notification("success", "Bookmark created successfully");
}