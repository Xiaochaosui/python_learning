<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>demo</title>
</head>
<script type="text/javascript" src="jquery.js"></script>
<script language="javascript">
	function get_mobile_code(){
        $.post('sms.jsp', {mobile:jQuery.trim($('#mobile').val()),send_code:$("#gd_code").val()}, function(msg) {
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
<form action="reg.jsp" method="post" name="formUser" onSubmit="return register();">
	<table width="100%"  border="0" align="left" cellpadding="5" cellspacing="3">
		<tr>
			<td align="right">手机<td>
		<input id="mobile" name="mobile" type="text" size="25" class="inputBg" /><span style="color:#FF0000"> *</span>
        </tr>
		   <tr>
	    	<td align="right">验证码</td>
	    	<td>
	    	<input type="text" name="gd_code" class="inputBg" size="25" id="gd_code" onkeyup="value=value.replace(/[^\d]/g,'')" placeholder="请输入正确的验证码">
	    	<span>&nbsp;<img src="code.jsp" onClick="javascript:this.src=this.src+'?date='+Date();" ></span>
	    	</td>
        </tr>
		<tr>
			<td align="right">手机验证码</td>
			<td align="left">
				<input type="text"  name="mobile_code" class="inputBg" size="25" />
				<input id="zphone" type="button" value=" 获取手机验证码 " style="width: 120px"  onClick="get_mobile_code()">
			</td>
		</tr>
	</table>
</form>
</body>
</html>