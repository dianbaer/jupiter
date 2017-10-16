function BlogMediator() {

    this.init = function (view) {

    }
    // 注销方法
    this.dispose = function () {


    }
    // 关心消息数组
    this.listNotificationInterests = [$T.notification.SEND_HTTP_START, $T.notification.SEND_HTTP_END, $T.notification.SYSTEM_ERROR];
    // 关心的消息处理
    this.handleNotification = function (data) {

    }
    this.advanceTime = function (passedTime) {

    }

}
$T.blogMediator = new BlogMediator();