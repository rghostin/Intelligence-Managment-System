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
                append_search_entry(entry, detail_view_endpoint)
            }
        },
        error: function () {
          display_notification("error", "UNable to load search results");
        }
    });
}

function ajax_load_all_resources(api_endpoint, detail_view_endpoint) {
    ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, null, null);
    hide_results_banner()
}


function make_tags_list_html(tags) {
    let tags_list_html = "<p>";
    for (i=0; i < tags.length; i++) {
        let tagname = tags[i];
        let tag_html = "<span class='badge badge-danger'>"+tagname + "</span>  ";
        tags_list_html += tag_html;
    }
    tags_list_html += "</p>"
    return tags_list_html;
}

function append_search_entry(entry, detail_view_endpoint) {
    let view_endpoint = detail_view_endpoint + entry.id;

    let tags_list = make_tags_list_html(entry.tags);
    let resource_type = capFirst(entry.resource_type);
    let note = "";
    if (entry.note) {
        note = entry.note;
    }

    let html_entry = `
    <tr>
        <td>
            <h4 class="h5 mt-3 mb-2">
                <a href="${view_endpoint}">#${entry.id} - ${entry.title}</a>
            </h4>
            <p class="d-none d-sm-block text-muted">
                ${note}
            </p>
        </td>
        <td class="d-none d-lg-table-cell text-center">${resource_type}</td>
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
        $("#id_div_prev").removeClass("disabled");
    } else {
        $("#id_prev").on("click", function () {
            return false;
        });
        $("#id_div_prev").addClass("disabled");
    }

    if (next_link) {
        $("#id_next").on("click", function () {
            ajax_load_filtered_intels(api_endpoint, detail_view_endpoint, curr_filterArray, curr_page+1);
        });
        $("#id_div_next").removeClass("disabled");
    } else {
        $("#id_next").on("click", function () {
            return false;
        });
        $("#id_div_next").addClass("disabled");
;

    }

}