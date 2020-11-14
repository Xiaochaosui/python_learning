/* *
 * 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
 * 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
 * 注意事项：
*（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
 *（2）请使用 用户名 及 APIkey来调用接口，APIkey在会员中心可以获取；
*（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
*/

/**
 * Created by XadillaX on 14-2-12.
 * https://github.com/XadillaX/ihuyi106js
 */
String.prototype.replaceAll = function(reallyDo, replaceWith, ignoreCase) {
    if (!RegExp.prototype.isPrototypeOf(reallyDo)) {
        return this.replace(new RegExp(reallyDo, (ignoreCase ? "gi": "g")), replaceWith);
    } else {
        return this.replace(reallyDo, replaceWith);
    }
};

var dom = require('xmldom').DOMParser;

var _baseUri = "http://106.ihuyi.com/webservice/sms.php?method=Submit";
var _userAgent = "node-ihuyi106-module by 死月 (admin@xcoder.in)";

/**
 * iHuyi constructure.
 * @param account
 * @param password 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
 */
var iHuyi = function(account, password) {
    this.spidex = require("spidex");
    this.spidex.setDefaultUserAgent(_userAgent);

    this.account = account;
    this.password = password;
};

/**
 * send an SMS.
 * @param mobile
 * @param content
 * @param callback
 */
iHuyi.prototype.send = function(mobile, content, callback) {
    var data = {
        account         : this.account,
        password        : this.password,
        mobile          : mobile,
        content         : content
    };

    this.spidex.post(_baseUri, {data:data}, function(html, status) {
        if(status !== 200) {
            callback(new Error("短信发送服务器响应失败。"));
            return;
        }

        html = html.replaceAll("\r", "");
        html = html.replaceAll("\n", "");
        html = html.replaceAll(" xmlns=\"http://106.ihuyi.com/\"", "");

        //console.log(html);
        var doc = new dom().parseFromString(html);
        var result = doc.lastChild;
        var json = {};
        for(var node = result.firstChild; node !== null; node = node.nextSibling) {
            json[node.tagName] = node.firstChild.data;
        }

        //console.log(json);
        if(json.code == "2") {
            callback(null, json.smsid);
        } else {
            callback(new Error(json.msg, parseInt(json.code)));
        }
    }, "utf8").on("err", function(e) {
        callback(e);
    });
};

module.exports = iHuyi;
