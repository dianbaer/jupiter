(function (window) {
    if (!window.jupiter) window.jupiter = {};
    var Mediator = window.juggle.Mediator;
    var demoProxy = window.jupiter.demoProxy;
    var RegisterMediator = function () {
        this.initView = function (view) {
            $("#registerButton").on('click', this.onRegister);
        };
        this.onRegister = function () {
            var userName = $("#userName").val();
            var userEmail = $("#userEmail").val();
            var userPassword = $("#userPassword").val();
            var userImg = $("#userImg")[0].files;
            demoProxy.demoTest(userName, userEmail, userPassword, userImg);
        };
        Mediator.apply(this);
    };
    window.jupiter.RegisterMediator = RegisterMediator;
})(window);