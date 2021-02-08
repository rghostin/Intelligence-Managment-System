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
          display_notification("error", "Unable to load search results");
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
    let description = "";
    if (entry.description) {
        description = truncateString(entry.description, 200);
    }
    let link = "<i class=\"fa fa-unlink mr-1\"></i>";
    if (entry.link) {
        link = `<a target='_blank' rel='noopener' href="${entry.link}" data-toggle="tooltip" title="${entry.link}" data-placement="top"><i class=\"fa fa-link mr-1\"></i></a>`;
    }

    let last_update = formatISO806(entry.last_update);

    let html_entry = `
        <tr>
            <td class="text-center" style="width: 60px; font-size: 18px;"><b>#${entry.id}</b></td>

            <td style="width:350px;">
                <a class="font-w400" href="${view_endpoint}" style="font-size: 18px">${entry.title}</a>
                <div class="text-muted mt-1">${description}</div>
            </td>
            
            <td class="d-none d-xl-table-cell text-muted" style="width: 70px;"><i class="fa fa-paperclip mr-1"></i> (${entry.files.length})</td>

            <td class="d-none d-xl-table-cell text-muted" style="width: 70px;">${link}</td>


            <td class="d-none d-sm-table-cell font-w600" style="width: 140px;">${tags_list}</td>


            <td class="d-none d-xl-table-cell text-muted" style="width: 130px;">
                <span class="font-size-sm">
                    by <a href="#">${entry.author}</a>
                    <br>
                    C <em>${entry.creation_date}</em>
                    <br>
                    U <em>${last_update}</em>
                </span>
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