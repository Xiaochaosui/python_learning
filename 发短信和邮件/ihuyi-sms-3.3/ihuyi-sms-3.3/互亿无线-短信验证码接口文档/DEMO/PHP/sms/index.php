<?php
  //接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
  //账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
  //注意事项：
  //（1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。；
  //（2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
  //（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

session_start();
date_default_timezone_set("PRC");

if(!empty($_GET['send_sms'])){
    include('sms.class.php');
    $sms = new ihuyi_sms;
    $sms -> send_sms($_POST['mobile'],$_POST['send_code']);
    die;
}

if($_POST){
	if($_POST['mobile']!=$_SESSION['mobile'] or $_POST['mobile_code']!=$_SESSION['mobile_code'] or empty($_POST['mobile']) or empty($_POST['mobile_code'])){
		exit('手机验证码输入错误。');
	}else{
		$_SESSION['mobile']			= '';
		$_SESSION['mobile_code']	= '';
		exit('注册成功。');
	}
}



?>
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>demo</title>
</head>
<script type="text/javascript" src="jquery.js"></script>
<script language="javascript">
	function get_mobile_code(){
        $.post('index.php?send_sms=1', {mobile:jQuery.trim($('#mobile').val()),send_code:$("#gd_code").val()}, function(msg) {
   		    alert(jQuery.trim(unescape(msg)));
			if(msg =='提交成功'){
				RemainTime();
			}else{
			//	location.reload();
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
<form action="index.php" method="post" name="formUser">
	<table width="100%"  border="0" align="left" cellpadding="5" cellspacing="3">
		<tr>
			<td align="right">手机</td>
			<td>
			<input id="mobile" name="mobile" type="text" size="25" class="inputBg" /><span style="color:#FF0000"> *</span> 
    	</td>
        </tr>
        <tr>
	    	<td align="right">验证码</td>
	    	<td>
	    	<input type="text" name="gd_code" class="inputBg" size="25" id="gd_code">
	    	<span>&nbsp;<img src="code.php" onClick="javascript:this.src=this.src+'?date='+Date();"></span>
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