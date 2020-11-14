<?php 

	/**
	 *  回执推送示例 
	 *	本示例仅供参考 请根据实际需求修改
	 *
	 *	用户先提供数据接收地址
	 *  然后绑定到互亿无线系统后台
	 *  平台会以 POST 方式实时的将回执信息推送到此地址
	 *
	 * 	不同回执推送参数可能不同 请根据文档修改
	 *
	 */

	date_default_timezone_set("PRC");
	if(empty($_POST['code'])) exit;

	$data = array();
	$data['code'] 		 = intval($_POST['code']);				//状态值 2为成功 其他为失败
	$data['msg'] 		 = strip_tags($_POST['msg']);			//回执说明
	$data['mobilephone'] = strip_tags($_POST['mobilephone']);	//手机号码
	$data['smsid'] 		 = strip_tags($_POST['smsid']);			//流水号  (对应提交时返回的 smsid)
	$data['report_time'] = strip_tags($_POST['report_time']);	//回执时间

	$file = 'ihuyi_log.txt';
	$text = date("Y-m-d H:i:s").' 回执参数: '.var_export($data,true).PHP_EOL;
	file_put_contents($file, $text,FILE_APPEND);



 ?>