(function (window) {
    if (!window.jupiter) window.jupiter = {};
    var Proxy = window.juggle.Proxy;
    var HttpClient = window.juggle.HttpClient;
    var httpEventType = window.juggle.httpEventType;
    var url = window.jupiter.url;
    var DemoProxy = function () {
        Proxy.apply(this);
        this.demoTest = function (userName, userEmail, userPassword, userImg) {
            var data = {
                "userName": userName,
                "userPassword": userPassword,
                'userEmail': userEmail
            };
            var packet = encodeURI(JSON.stringify(data));
            data["packet"] = packet;
            var httpClient = new HttpClient();
            if (userImg !== null && userImg.length !== 0) {
                httpClient.sendFile(userImg, data, url.createExample, null);
            } else {
                httpClient.send(data, url.createExample, null);
            }
            httpClient.addEventListener(httpEventType.SUCCESS, this.demoTestSuccess, this);
            httpClient.addEventListener(httpEventType.ERROR, this.demoTestFail, this);
        };
        this.demoTestSuccess = function (event) {
            alert("返回成功" + event.mData);
        };
        this.demoTestFail = function (event) {
            alert("返回失败")
        }
    };
    window.jupiter.demoProxy = new DemoProxy();
})(window);