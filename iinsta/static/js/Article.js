var Article = function(element) {
    var _this = this;
    _this.element = element;
    _this.likeButton = element.querySelector('.btn-like');
    _this.commentButton = element.querySelector('.btn-comment');
    _this.buttonMore = element.querySelector('.btn-more');

    _this.buttonMore.addEventListener('click', function(e) {
        console.log('more');
    });

    _this.likeButton.addEventListener('click', function(e) {
        console.log('like');
    });

    _this.commentButton.addEventListener('click', function(e) {
        console.log('comment');
    });
};
