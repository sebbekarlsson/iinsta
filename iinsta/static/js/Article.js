var Article = function(element) {
    var _this = this;
    _this.element = element;
    _this.likeButton = element.querySelector('.btn-like');
    _this.commentButton = element.querySelector('.btn-comment');
    _this.commentPublishButton = element.querySelector('.btn-comment-publish');
    _this.commentInput = element.querySelector('.new-comment input[type="text"]');
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

    _this.commentPublishButton.addEventListener('click', function(e) {
        console.log('publish comment');

        _this.commentInput.value = '';
    });
};
