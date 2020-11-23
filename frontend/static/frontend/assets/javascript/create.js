function create_intel(api_endpoint, data) {
    $.ajax({
        type: "POST",
        url: api_endpoint,
        data: data,
        success: function(data) {
           console.log(0);
           console.log(data);
           console.log(data.id);
           // upload_files(data.id);
        }
    });
}

function add_file_to_table(file) {
    console.log(file);
     $("#id_files_table tbody").prepend(
        "<tr><td>"+file.name+"</td><td>"+file.type+"</td><td>"+file.size+"</td></tr>"
    )
}
