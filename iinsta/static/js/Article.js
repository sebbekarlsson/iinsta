var MoreMenu = function(article, element) {
    var _this = this;
    _this.article = article;
    _this.element = element;
    _this.buttons = element.querySelectorAll('button');

    _this.toggle = function() {
        if (_this.element.getAttribute('data-active') == '0') {
            _this.element.setAttribute('data-active', '1');
        } else {
            _this.element.setAttribute('data-active', '0');
        }
    };

    for (var i = 0; i < _this.buttons.length; i++) {
        var btn = _this.buttons[i];

        if (btn.hasAttribute('data-delete')) {
            btn.addEventListener('click', _this.article.onDelete);
        }
    }
};


var Article = function(element) {
    var _this = this;
    _this.element = element;
    _this.dataId = element.getAttribute('data-id');
    _this.likeButton = element.querySelector('.btn-like');
    _this.infoLikes = element.querySelector('.info-likes');
    _this.commentButton = element.querySelector('.btn-comment');
    _this.commentPublishButton = element.querySelector('.btn-comment-publish');
    _this.commentInput = element.querySelector('.new-comment input[type="text"]');
    _this.commentsSection = element.querySelector('.article-comments');
    _this.newCommentSection = element.querySelector('.new-comment');
    _this.buttonMore = element.querySelector('.btn-more');
    _this.moreMenu = element.querySelector('.menu-more');

    
    _this.buttonMore.addEventListener('click', function(e) {
        _this.toggleMoreMenu();
    });

    _this.likeButton.addEventListener('click', function(e) {
        console.log('like');

        wget('/api/article/like/' + _this.dataId, function(data) {
            data = JSON.parse(data);
            console.log(data);
            _this.refresh();
        });
    });

    _this.commentButton.addEventListener('click', function(e) {
        _this.newCommentSection.setAttribute('data-active', 1);
        _this.commentInput.focus();
    });

    _this.toggleMoreMenu = function() {
        _this.menu.toggle(); 
    };

    _this.refresh = function() {
        _this.commentsSection.innerHTML = '';

        wget('/api/article/' + _this.dataId, function(data) {
            data = JSON.parse(data);

            if (!data)
                return _this.element.parentNode.removeChild(_this.element);

            _this.infoLikes.innerText = data.likers.length;

            for (i = 0; i < data.comments.length; i++) {
                var comment = data.comments[i];

                var element = "<li><span>" + comment.user.name + "</span><span>" + comment.content + "</span></li>";
                _this.commentsSection.innerHTML += element;
            }
        });
    };

    _this.onDelete = function(e) {
        wget('/api/article/delete/' + _this.dataId, function(data) {
            data = JSON.parse(data);
            console.log(data);
            _this.refresh();
        });
    };

    _this.commentPublishButton.addEventListener('click', function(e) {
        wpost('/api/article/comment/' + _this.dataId, {
            'content': _this.commentInput.value
        }, function(data) {
            _this.refresh();
        });

        _this.commentInput.value = '';
    });
    
    _this.menu = new MoreMenu(_this, _this.moreMenu);
};
