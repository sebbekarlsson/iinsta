var Account = function(element) {
    var _this = this;
    _this.element = element;
    _this.moreButton = element.querySelector('.btn-more');
    
    _this.moreButton.addEventListener('click', function(e) {
        e.preventDefault();

        console.log('more');
    });
};
