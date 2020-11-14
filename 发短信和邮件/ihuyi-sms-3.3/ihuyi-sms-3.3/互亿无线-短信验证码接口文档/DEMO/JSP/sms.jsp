<%@ page contentType="text/html" pageEncoding="UTF-8"%><%@ page import = "java.io.*" %><%@ page import = "java.net.*" %><%@ page import = "java.util.*" %><%@ page import = "java.lang.*" %><%

 // 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
 // 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
 // 注意事项：
 //（1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。；
 //（2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
 //（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

String postUrl = "http://106.ihuyi.cn/webservice/sms.php?method=Submit";

int mobile_code = (int)((Math.random()*9+1)*100000); //获取随机数

String account = "用户名"; //查看用户名是登录用户中心->验证码短信->产品总览->APIID
String password = "密码";  //查看密码请登录用户中心->验证码短信->产品总览->APIKEY
String mobile = request.getParameter("mobile");
String content = new String("您的验证码是：" + mobile_code + "。请不要把验证码泄露给其他人。");
String send_code = request.getParameter("send_code");
String session_code = (String)session.getAttribute("randStr");

// 此处验证码仅限于纯数字比对
if (Integer.parseInt(send_code) != Integer.valueOf(session_code)) {
	String message = new String("请输入正确的验证码");
	out.println(message);
	return;
}

try {

	URL url = new URL(postUrl);
	HttpURLConnection connection = (HttpURLConnection) url.openConnection();
	connection.setDoOutput(true);//允许连接提交信息
	connection.setRequestMethod("POST");//网页提交方式“GET”、“POST”
	connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
	connection.setRequestProperty("Connection", "Keep-Alive");
	StringBuffer sb = new StringBuffer();
	sb.append("account="+account);
	sb.append("&password="+password);
	sb.append("&mobile="+mobile);
	sb.append("&content="+content);
	OutputStream os = connection.getOutputStream();
	os.write(sb.toString().getBytes());
	os.close();

	String line, result = "";
	BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "utf-8"));
	while ((line = in.readLine()) != null) {
		result += line + "\n";
	}
	in.close();
	out.println(result);

} catch (IOException e) {
	e.printStackTrace(System.out);
}

%>