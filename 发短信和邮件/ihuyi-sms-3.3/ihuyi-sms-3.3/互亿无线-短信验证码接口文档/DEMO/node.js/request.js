var request     = require('request');
var url         ="http://106.ihuyi.com/webservice/sms.php?method=Submit";
var requestData ={account:'apiid',password:'apikey',mobile:'手机号',content:'您的验证码是：000000。请不要把验证码泄露给其他人。',format:'json'};
 
httprequest(url,requestData);
 
function httprequest(url,data){
    request({
        url: url,
        method: "POST",
        json: true,
        headers: {
            "content-type": "application/json",
        },
        form: requestData
    }, function(error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body) // 请求成功的处理逻辑
        }
    });
};