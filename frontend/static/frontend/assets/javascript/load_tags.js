function load_tags() {
    // serialize tag options
    var tag_options = {}
    var select_elem = document.getElementById("id_tags");
    for (let i = 0; i < select_elem.options.length; i++) {
        let tag_option = select_elem.options[i];
        tag_options[tag_option.value] = {"text": tag_option.innerText, "selected": tag_option.selected};
    }
    console.log(tag_options)

    // init suggestion engine
    var engine_entry = []
    for (let option_val in tag_options) {
        engine_entry.push({id: option_val, text: tag_options[option_val]["text"]});
    }

    var tagnames =  new Bloodhound({
        local:  engine_entry,
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('text'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
    });
    var promise = tagnames.initialize();
    // promise .done(function() { console.log('load OK!'); }).fail(function() { console.log('load ERR'); });

    // init tagsinput
    $('#id_tags').tagsinput({
        // tagClass: "",
        trimValue: true,
        allowDuplicates: false,
        freeInput: false,
        itemValue: 'id',
        itemText: 'text',
        typeaheadjs: {
           name: 'tagnames',
           displayKey: 'text',
           source: tagnames.ttAdapter()
        }
    });

    // fill initial tags
    $('#id_tags').tagsinput("removeAll");
    for (let option_val in tag_options) {
        if (tag_options[option_val]["selected"]) {
            $('#id_tags').tagsinput('add', {id: option_val, text: tag_options[option_val]["text"]});
        }
    }
}