function create_intel(api_endpoint, data) {
    console.log(data);

    $.ajax({
        type: "POST",
        url: api_endpoint,
        data: data,
        success: function(data) {
               console.log(0);
               console.log(data);
            }
    });
}