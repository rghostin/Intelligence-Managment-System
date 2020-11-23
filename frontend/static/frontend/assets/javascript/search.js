function ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, filter) {
    let show_results_banner = false;
    if (filter != null) {
        show_results_banner = true;
    }
    $.ajax({
        url: api_endpoint,
        contentType: "application/json",
        dataType: 'json',
        data: filter,
        beforeSend: function(jqXHR, settings) {console.log(settings.url);},
        success: function(data){
            $('#id_search_results_body').empty();
            for (let i = 0; i < data.count; i++) {
                let entry = data.results[i];
                append_search_entry(entry, detail_view_endpoint)
            }

            if (show_results_banner) {
                display_results_banner(data.count);
            }
        }
        // todo error
    });
}

function ajax_load_all_resources(api_endpoint, detail_view_endpoint) {
    ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, null);
    hide_results_banner()
}

function append_search_entry(entry, detail_view_endpoint) {
    let view_endpoint = detail_view_endpoint + entry.id;
    console.log(entry.tags);
    let tags_list = entry.tags.map(function(elem){return elem.name;}).join(",");

    let html_entry = `
    <tr>
        <td>
            <h4 class="h5 mt-3 mb-2">
                <a href="${view_endpoint}">${entry.title}</a>
            </h4>
            <p class="d-none d-sm-block text-muted">

            </p>
        </td>


        <td class="d-none d-lg-table-cell text-center">#article</td>
        <td>${tags_list}</td>
        <td class="d-none d-lg-table-cell font-size-xl text-center font-w600">
            <a href=\"${entry.link}\">Link</a>
        </td>

    </tr>
    `;

    $('#id_search_results_body').append(html_entry);
}

function display_results_banner(number) {
    $('#id_results_banner').show();
    $('#id_results_banner_number').text(number.toString());
}

function hide_results_banner() {
    $('#id_results_banner').hide();
}