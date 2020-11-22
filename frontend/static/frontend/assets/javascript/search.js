function ajax_load_all_resources(endpoint) {
    $.ajax({
        url: endpoint,
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            $('#id_search_results_body').empty();
            for (let i = 0; i < data.count; i++) {
                let entry = data.results[i];
                append_search_entry(
                    entry.title,
                    entry.link
                )
            }
        }
    });
}

function append_search_entry(title, link) {
    let entry = `
    <tr>
        <td>
            <h4 class="h5 mt-3 mb-2">
                <a href="javascript:void(0)">${title}</a>
            </h4>
            <p class="d-none d-sm-block text-muted">

            </p>
        </td>


        <td class="d-none d-lg-table-cell text-center">
        </td>
        <td class="d-none d-lg-table-cell font-size-xl text-center font-w600">
            <a href=\"${link}\">Link</a>
        </td>

    </tr>
    `;

    $('#id_search_results_body').append(entry);
}
