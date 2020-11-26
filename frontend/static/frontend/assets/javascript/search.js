function ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, filterArray, page) {
    let show_results_banner = false;
    if (filterArray) {
        show_results_banner = true;
    }

    let data = [];
    if (filterArray) {
        data = data.concat(filterArray)
    }
    if (page) {
        data.push({name: "page", value: page})
    }

    $.ajax({
        url: api_endpoint,
        contentType: "application/json",
        dataType: 'json',
        data: $.param(data),
        beforeSend: function(jqXHR, settings) {console.log(settings.url);},
        success: function(data){
            if (show_results_banner) {
                display_results_banner(data.count);
            }

            load_pagination(api_endpoint, detail_view_endpoint, filterArray, page, data.previous, data.next);

            $('#id_search_results_body').empty();
            for (let i = 0; i < data.results.length; i++) {
                let entry = data.results[i];
                console.log("entry "+entry);
                append_search_entry(entry, detail_view_endpoint)
            }
        }
        // todo error
    });
}

function ajax_load_all_resources(api_endpoint, detail_view_endpoint) {
    ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, null, null);
    hide_results_banner()
}

function append_search_entry(entry, detail_view_endpoint) {
    let view_endpoint = detail_view_endpoint + entry.id;
    console.log(entry.tags);
    let tags_list = entry.tags.join(",");

    let html_entry = `
    <tr>
        <td>
            <h4 class="h5 mt-3 mb-2">
                <a href="${view_endpoint}">${entry.title}</a>
            </h4>
            <p class="d-none d-sm-block text-muted">
                lorem
            </p>
        </td>


        <td class="d-none d-lg-table-cell text-center">${entry.resource_type}</td>
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

function set_page_num(num) {
    $("#id_page_num").text(num.toString());
}

function load_pagination(api_endpoint, detail_view_endpoint, curr_filterArray, curr_page, prev_link, next_link) {
    if (!curr_page){
        curr_page=1;
    }
    set_page_num(curr_page);

    $("#id_prev").off();
    $("#id_next").off()

    if (prev_link) {
        $("#id_prev").on("click", function () {
            ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, curr_filterArray, curr_page-1);
        });
    } else {
        $("#id_prev").on("click", function () {
            return false;
        });
    }

    if (next_link) {
        $("#id_next").on("click", function () {
            ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, curr_filterArray, curr_page+1);
        });
    } else {
        $("#id_next").on("click", function () {
            return false;
        });
    }

}