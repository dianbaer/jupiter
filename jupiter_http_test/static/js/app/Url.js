(function (window) {
    if (!window.jupiter) window.jupiter = {};
    var Url = function () {
        this.createExample = "/api/examples";
    };
    window.jupiter.url = new Url();
})(window);