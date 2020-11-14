<%@LANGUAGE="VBSCRIPT" CODEPAGE="936"%>
<%

 '接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
 '账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
 '注意事项：
 '（1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。；
 '（2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及APIkey来调用接口；
 '（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

'生成随机数
Function gen_key(digits)
	dim char_array(50)
	char_array(0) = "0"
	char_array(1) = "1"
	char_array(2) = "2"
	char_array(3) = "3"
	char_array(4) = "4"
	char_array(5) = "5"
	char_array(6) = "6"
	char_array(7) = "7"
	char_array(8) = "8"
	char_array(9) = "9"
	randomize
	do while len(output) < digits
	num = char_array(Int((9 - 0 + 1) * Rnd + 0))
	output = output + num
	loop
	gen_key = output
End Function

send_code = gen_key(4)
Session("send_code") = send_code

mobile = request.Form("mobile")
if mobile<>"" then
	if Session("mobile_code")="" or Session("mobile_code")<>request.Form("mobile_code") or Session("mobile")="" or Session("mobile")<>request.Form("mobile") then
		response.Write("手机验证码输入错误")
	else
		response.Write("注册成功")
	end if

end if
%>
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=gb2312" />
<title>demo</title>
</head>
<script type="text/javascript" src="jquery.js"></script>
<script language="javascript">
	function get_mobile_code(){
        $.post('sms.asp', {mobile:jQuery.trim($('#mobile').val()),send_code:$("#gd_code").val()}, function(msg) {
            alert(jQuery.trim(unescape(msg)));
			if(msg=='提交成功'){
				RemainTime();
			}else{
				location.reload();
			}
        });
	};
	var iTime = 59;
	var Account;
	function RemainTime(){
		document.getElementById('zphone').disabled = true;
		var iSecond,sSecond="",sTime="";
		if (iTime >= 0){
			iSecond = parseInt(iTime%60);
			iMinute = parseInt(iTime/60)
			if (iSecond >= 0){
				if(iMinute>0){
					sSecond = iMinute + "分" + iSecond + "秒";
				}else{
					sSecond = iSecond + "秒";
				}
			}
			sTime=sSecond;
			if(iTime==0){
				clearTimeout(Account);
				sTime='获取手机验证码';
				iTime = 59;
				document.getElementById('zphone').disabled = false;
			}else{
				Account = setTimeout("RemainTime()",1000);
				iTime=iTime-1;
			}
		}else{
			sTime='没有倒计时';
		}
		document.getElementById('zphone').value = sTime;
	}	
</script>
<body>
<form action="reg.asp" method="post" name="formUser" onSubmit="return register();">
	<table width="100%"  border="0" align="left" cellpadding="5" cellspacing="3">
		<tr>
		<td align="right">手机<td>
			<input id="mobile" name="mobile" type="text" size="25" class="inputBg" /><span style="color:#FF0000"> *</span> 
        </tr>
		<tr>
			<td align="right">验证码</td>
			<td>
			<input type="text" name="gd_code" class="inputBg" size="25" id="gd_code">
			<span>&nbsp;<img src="code.asp" onClick="javascript:this.src=this.src+'?date='+Date();"></span>
			</td>
		</tr>
			<tr>
			<td align="right">手机验证码</td>
			<td align="left">
			<input type="text"  name="mobile_code" class="inputBg" size="25" />
			<input id="zphone" type="button" value=" 获取手机验证码 " style="width: 120px"  onClick="get_mobile_code()">
			</td>
		</tr>
		<tr>
			<td align="right"></td>
			<td><input type="submit" value=" 注册 " class="button"></td>
		</tr>
	</table>
</form>
</body>
</html>