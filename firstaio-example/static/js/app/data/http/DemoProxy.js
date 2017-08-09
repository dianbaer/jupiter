function DemoProxy() {
    this.demoTest = function (userName, userEmail, userPassword, userImg) {
        var data = {
            "userName": userName,
            "userPassword": userPassword,
            'userEmail': userEmail
        };

        var sendParam = new SendParamNormal();
        sendParam.successHandle = this.demoTestSuccess;
        sendParam.failHandle = this.demoTestFail;
        sendParam.object = this;
        sendParam.data = data;
        sendParam.url = '/api/users';
        if (userImg != null && userImg.length != 0) {
            sendParam.fileArray = userImg;
        }
        $T.httpUtilNormal.send(sendParam);
    }
    this.demoTestSuccess = function (result, sendParam) {
        alert("返回成功" + JSON.stringify(result));
    }
    this.demoTestFail = function (result, sendParam) {
        alert("返回失败")
    }
}
$T.demoProxy = new DemoProxy();