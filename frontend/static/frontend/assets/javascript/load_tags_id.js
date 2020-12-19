function load_suggestion_engine() {
    return new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch: {
            url: '/api/tags/?format=json',
            filter: function(data) {
                return $.map(data.results, function(tag_entry) {
                    return {id:tag_entry.id,  name:tag_entry.name} ;
                });
            },
            ttl: 0
        }
    });
}


function load_tags_id() {
    let engine = load_suggestion_engine()
    let promise = engine.initialize();
    promise
        .fail(function () {console.error("unable to initialize suggestion engine");})
        .done(function () {
            console.log("ok");
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
                   source: engine.ttAdapter()
                }
            });
        });
}