function load_suggestion_engine() {
    return new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        // prefetch: {
        //     url: '/api/tags/?format=json',
        //     filter: function(data) {
        //         return $.map(data.results, function(tag_entry) {   return tag_entry.name; });
        //     },
        //     ttl: 0
        // }
         remote: {
            url: '/api/tags/?format=json&search=%QUERY',
            wildcard: '%QUERY',
            filter: function(data) {
                return $.map(data.results, function(tag_entry) { return tag_entry.name; });
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
            // init tagsinput
            $('#id_tags').tagsinput({
                tagClass: "badge badge-primary",
                trimValue: true,
                allowDuplicates: false,
                freeInput: false,
                typeaheadjs: {
                   name: 'tagnames',
                   source: engine,
                   templates: {
                        empty: [
                          '<div>No matching tags found</div>'
                        ].join('\n'),
                        suggestion: function(data){
                            return '<span class="badge badge-secondary">' + data + '</span>';
                        }
                  }
                }
            });
        });
}