function ajax_load_filtered_resources(api_endpoint, detail_view_endpoint, keyword) {
    let show_results_banner = false;
    if (keyword != null) {
        api_endpoint = api_endpoint + "?search="+keyword;
        show_results_banner = true;
    }
    $.ajax({
        url: api_endpoint,
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            $('#id_search_results_body').empty();
            for (let i = 0; i < data.count; i++) {
                let entry = data.results[i];
                append_search_entry(entry, detail_view_endpoint)
            }

            if (show_results_banner) {
                display_results_banner(data.count, keyword);
            }
        }
    });
}

function ajax_load_all_resources(api_endpoint, detail_view_endpoint) {
    ajax_load_filtered_resources(api_endpoint, detail_view_endpoint, null);
    hide_results_banner()
}

function append_search_entry(entry, detail_view_endpoint) {
    let view_endpoint = detail_view_endpoint + entry.id;
    let html_entry = `
    <tr>
        <td>
            <h4 class="h5 mt-3 mb-2">
                <a href="${view_endpoint}">${entry.title}</a>
            </h4>
            <p class="d-none d-sm-block text-muted">

            </p>
        </td>


        <td class="d-none d-lg-table-cell text-center">
        </td>
        <td class="d-none d-lg-table-cell font-size-xl text-center font-w600">
            <a href=\"${entry.link}\">Link</a>
        </td>

    </tr>
    `;

    $('#id_search_results_body').append(html_entry);
}

function display_results_banner(number, keyword) {
    $('#id_results_banner').show();
    $('#id_results_banner_number').text(number.toString());
    $('#id_results_banner_keyword').text(keyword);
}

function hide_results_banner() {
    $('#id_results_banner').hide();
}