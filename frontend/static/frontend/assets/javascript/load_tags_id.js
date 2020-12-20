function load_suggestion_engine() {
    return new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        // prefetch: {
        //     url: '/api/tags/?format=json',
        //     filter: function(data) {
        //         return $.map(data.results, function(tag_entry) {
        //             return {id:tag_entry.id,  name:tag_entry.name} ;
        //         });
        //     },
        //     ttl: 0
        // }
        remote: {
            url: '/api/tags/?format=json&search=%QUERY',
            wildcard: '%QUERY',
            filter: function(data) {
                return $.map(data.results, function(tag_entry) {
                    return {id:tag_entry.id,  name:tag_entry.name} ;
                });
            },
            ttl: 0
        }
    });
}


function load_tags() {
    let engine = load_suggestion_engine()
    let promise = engine.initialize();
    promise
        .fail(function () {console.error("unable to initialize suggestion engine");})
        .done(function () {

            // serialize tag options
            var tag_options = {}
            var select_elem = document.getElementById("id_tags");
            for (let i = 0; i < select_elem.options.length; i++) {
                let tag_option = select_elem.options[i];
                tag_options[tag_option.value] = {"name": tag_option.innerText, "selected": tag_option.selected};
            }

            // init tagsinput
            $('#id_tags').tagsinput({
                tagClass: "badge badge-primary",
                trimValue: true,
                allowDuplicates: false,
                freeInput: false,

                itemValue: 'id',
                itemText: 'name',
                typeaheadjs: {
                   name: 'tagnames',
                   displayKey: 'name',
                   source: engine.ttAdapter(),
                   templates: {
                        empty: [
                          '<div>No matching tags found</div>'
                        ].join('\n'),
                        suggestion: function(data){
                            return '<span class="badge badge-secondary">' + data.name + '</span>';
                        }
                  }
                }
            });

             // fill initial tags
            $('#id_tags').tagsinput("removeAll");
            for (let option_val in tag_options) {
                if (tag_options[option_val]["selected"]) {
                    $('#id_tags').tagsinput('add', {id: option_val, name: tag_options[option_val]["name"]});
                }
            }
        });
}