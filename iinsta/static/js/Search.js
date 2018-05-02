var Search = function(input, button, resultsDOM) {
    var _this = this;
    _this.input = input;
    _this.button = button;
    _this.resultsDOM = resultsDOM;

    _this.button.addEventListener('click', function(e) {
        var query = _this.input.value;
        _this.input.value = '';

        wget('/api/search/' + query, function(data) {
            var json = JSON.parse(data);

            console.log(data);

            _this.resultsDOM.innerHTML = '';
            for (var i = 0; i < json.length; i++) {
                var obj = json[i];

                var element = '';

                if (typeof obj == 'string') {
                    element = _this.createResultsItem(obj, 'hashtag');
                } else {
                    element = _this.createResultsItem(obj['name'], 'user', '/uploads/' + (obj['avatar'] ? obj['avatar']['filename'] : ''));
                }
                _this.resultsDOM.innerHTML += element;
            }
        });
    });

    _this.createResultsItem = function(name, type, image) {
        var dom = ["<a href='" + (type == 'user' ? ('/' + name) : ('/feed/' + name)) + "' class='search-results-list-item'>",
            type == 'user' ? "<section>" : '',
            type == 'user' ? "<span class='circle' style='background-image:url("+ image +")'></span>": '',
            type == 'user' ? "</section>" : '',
            "<section><b>" + (type == 'hashtag' ? '#' : '') + name + "</b></section>",
            "</a>"].join('');

        console.log(dom);
        return dom;
    }
};
