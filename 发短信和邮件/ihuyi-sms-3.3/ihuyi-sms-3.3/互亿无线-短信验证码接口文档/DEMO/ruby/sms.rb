#接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
#账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
#注意事项：
#（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
#（2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
#（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
# 该代码仅供学习和研究接口使用，只是提供了一个参考

require 'typhoeus'

# 接口地址
url="http://106.ihuyi.com/webservice/sms.php?method=Submit"

#用户名 查看用户名是登录用户中心->验证码短信->产品总览->APIID
account="用户名"
#密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password="密码"

body={account:account,password:password,mobile:"138xxxxxxxx",content:"您的验证码是：1212。请不要把验证码泄露给其他人。"}

resp=Typhoeus::Request.post(api_send_url,body:body)
puts resp.body