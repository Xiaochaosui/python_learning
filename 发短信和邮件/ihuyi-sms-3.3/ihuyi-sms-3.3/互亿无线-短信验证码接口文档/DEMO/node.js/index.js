//接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
// 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
// 注意事项：
//（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
//（2）请使用 用户名(例如：cf_demo123)及 APIkey来调用接口，APIkey在会员中心可以获取；
//（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

//npm install xmldom
//npm install spidex

var iHuyi = require("./lib/ihuyi");
var i = new iHuyi('apiid','apikey');

i.send('帐号','asdfsafsdaf',callback);

function callback(res){
    console.log(res);
}