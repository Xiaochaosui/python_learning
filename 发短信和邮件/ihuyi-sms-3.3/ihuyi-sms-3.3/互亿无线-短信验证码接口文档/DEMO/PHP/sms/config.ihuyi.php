<?php 

/**
*	@appid								互亿无线apiid
*	@appkey								互亿无线apikey
*	@sms_send_time						两次短信发送时间间隔 单位：秒
*	@sms_send_num						最大发送次数
*	@sms_send_black_time				限制发送时间 单位：秒 (一小时为 60*60 = 3600 秒)
*	@url								接口地址
*	@is_open_send_limit					是否开启发送限制（1开启 0关闭）
*/
	$GLOBALS['ihuyi']['appid']					= '';
	$GLOBALS['ihuyi']['appkey']					= '';
	$GLOBALS['ihuyi']['sms_send_time']			= 60;
	$GLOBALS['ihuyi']['sms_send_num']			= 5;
	$GLOBALS['ihuyi']['sms_send_black_time']	= 600;
	$GLOBALS['ihuyi']['url']					= "http://106.ihuyi.cn/webservice/sms.php?method=Submit";
	$GLOBALS['ihuyi']['is_open_send_limit']		= 1;