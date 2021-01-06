function bookmark_add (api_endpoint, csrftoken, intel_id, link) {
      $.ajax({
            url: api_endpoint,
            dataType: 'json',
            method: 'POST',
            headers: {
                'X-CSRFTOKEN': csrftoken
            },
            data: {"intel_id": intel_id, "link": link},
            beforeSend: function() { spinner_rotate_show(); },
            complete: function () { spinner_rotate_hide(); },
            success: function(data){
                console.log(data)},
            error: function () {
                display_notification("error", "Unable to save bookmark");
            }
        });
}