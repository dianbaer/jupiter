(function (window) {
    if (!window.jupiter) window.jupiter = {};
    var Mediator = window.juggle.Mediator;
    var BlogMediator = function () {
        Mediator.apply(this);
    };
    window.jupiter.BlogMediator = BlogMediator;
})(window);