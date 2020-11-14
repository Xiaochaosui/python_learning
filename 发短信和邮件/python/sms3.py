#接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
#账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
#注意事项：
#（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
#（2）请使用 用户名 及 APIkey来调用接口，APIkey在会员中心可以获取；
#（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
  
#!/usr/local/bin/python
#-*- coding:utf-8 -*-

import urllib2
import urllib
#用户名 查看用户名请登录用户中心->验证码、通知短信->帐户及签名设置->APIID
account  = "用户名" 
#密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "密码"
mobile = "138xxxxxxxx"
text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
data = {'account': account, 'password' : password, 'content': text, 'mobile':mobile,'format':'json' }
req = urllib2.urlopen(
url= 'http://106.ihuyi.com/webservice/sms.php?method=Submit',
data= urllib.urlencode(data)
)
content =req.read()
print(content)