var Article = function(element) {
    var _this = this;
    _this.element = element;
    _this.dataId = element.getAttribute('data-id');
    _this.likeButton = element.querySelector('.btn-like');
    _this.commentButton = element.querySelector('.btn-comment');
    _this.commentPublishButton = element.querySelector('.btn-comment-publish');
    _this.commentInput = element.querySelector('.new-comment input[type="text"]');
    _this.commentsSection = element.querySelector('.article-comments');
    _this.newCommentSection = element.querySelector('.new-comment');
    _this.buttonMore = element.querySelector('.btn-more');

    _this.buttonMore.addEventListener('click', function(e) {
        console.log('more');
    });

    _this.likeButton.addEventListener('click', function(e) {
        console.log('like');
    });

    _this.commentButton.addEventListener('click', function(e) {
        console.log('comment');
        _this.newCommentSection.setAttribute('data-active', 1);
        _this.commentInput.focus();
    });

    _this.refreshComments = function() {
        _this.commentsSection.innerHTML = '';

        wget('/api/article/' + _this.dataId, function(data) {
            data = JSON.parse(data);

            for (i = 0; i < data.comments.length; i++) {
                var comment = data.comments[i];

                var element = "<li><span>" + comment.user.name + "</span><span>" + comment.content + "</span></li>";
                _this.commentsSection.innerHTML += element;
            }
        });
    };

    _this.commentPublishButton.addEventListener('click', function(e) {
        console.log('publish comment');

        wpost('/api/article/comment/' + _this.dataId, {
            'content': _this.commentInput.value
        }, function(data) {
            console.log(data);
            _this.refreshComments();
        });

        _this.commentInput.value = '';
    });
};
