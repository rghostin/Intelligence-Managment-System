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
