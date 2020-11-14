<?php
class Code{
	private $fontSize;			//字体大小
	private $width;  			//画布宽度
	private $heigth;  			//画布高度
	private $sum;   			//验证码位数
	private $img;   			//图片资源
	private $code = array();	//验证码
	public $type = 0;			//验证码类型 0.纯数字  1.纯字母  2.混合  (设定了自定义字符集时无效)
	public $font = 4;			//选择字体  1-5
	public $str = NULL; 		//自定义验证码字符集 
	public $inCurve = true;		//是否画干扰曲线
	public $inNoise = true;		//是否画干扰字母
	
	/**
	 * 初始化验证码对象
	 * @param int $size 字体大小
	 * @param int $sum 验证码数量
	 */
	public function __construct($size=20,$sum = 4){
		$this->sum = $sum;
		$this->fontSize =  !empty($_GET['codeSize'])? $_GET['codeSize']:$size;
		$this->width = $this->fontSize*$this->sum;
		$this->heigth = $this->fontSize*1.5;
	}
	
	/**
	 * 取验证码图片
	 * @return void
	 */
	public function getImage(){
		//生存验证码
		$this->createCode();
		//创建画布
		$this->createImage();
		//干扰字母
		$this->createNoise();
		//干扰曲线1
		$this->createCurve();
		//写入字符串
		$this->printString();
		//干扰曲线2
		//$this->createCurve();
		//输出验证码图片
		header('Cache-Control: private, max-age=0, no-store, no-cache, must-revalidate');
        header('Cache-Control: post-check=0, pre-check=0', false);
        header('Pragma: no-cache');
        header("content-type: image/png");
		imagepng ($this->img);
	}
	/**
	 * 校验验证码是否正确 (正确返回 True,错误返回原因)  
	 * @param string $code  用户输入的验证码
	 * @param ing $new_time 指定过期时间(秒)
	 * @return bool
	 */
	static function check($code,$now_time = 1800){
		//是否为空
		if(empty($code) || empty($_SESSION['vcode'])){
			return false;
		}
		//是否过期
		if(time() - $_SESSION['vtime'] > $now_time){
			return false;
		}
		//输入是否正确
		if(md5($code) == $_SESSION['vcode']){
			return true;
		}
		return false;
	}
	
	/**
	 * 创建背景图像
	 */
	private function createImage(){
		$this->img = imagecreatetruecolor($this->width, $this->heigth);
		$color = imagecolorallocate($this->img, rand(150, 199), rand(150, 255), rand(150, 255));
		imagefill($this->img, 1, 1, $color);
	}

	/**
	 * 画干扰
	 */
	private function createNoise(){
		if(!$this->inNoise) return;
		$codeSet = '2345678abcdefhijkmnpqrstuvwxyz';
		$noiseSum = strlen($codeSet)-1;
        for($i = 0; $i < 5; $i++){
            //杂点颜色
            $noiseColor = imagecolorallocate($this->img, mt_rand(150,225), mt_rand(150,225), mt_rand(150,225));
            for($j = 0; $j < 2; $j++) {
                // 绘杂点
                imagestring($this->img, 5, mt_rand(-10, $this->width),  mt_rand(-10, $this->heigth), $codeSet[mt_rand(0, $noiseSum)], $noiseColor);
            }
        }
	}
	/**
	 * 画干扰曲线
	 */
	private function createCurve() {
		//判断用户设定
		if(!$this->inCurve) return;
        $px = $py = 0;
        // 曲线前部分
        $A = mt_rand(1, $this->heigth/2);                  // 振幅
        $b = mt_rand(-$this->width/4, $this->heigth/4);   // Y轴方向偏移量
        $f = mt_rand(-$this->heigth/4, $this->heigth/4);   // X轴方向偏移量
        $T = mt_rand($this->heigth, $this->width*2);  // 周期
        $w = (2* M_PI)/$T;
                        
        $px1 = 0;  // 曲线横坐标起始位置
        $px2 = mt_rand($this->width/2, $this->width * 2);  // 曲线横坐标结束位置
		$color = imagecolorallocate($this->img, rand(1, 100), rand(50, 150), rand(50, 150));
        for ($px=$px1; $px<=$px2; $px = $px + 1) {
            if ($w!=0) {
                $py = $A * sin($w*$px + $f)+ $b + $this->heigth/2;  // y = Asin(ωx+φ) + b ??
                $i = (int) ($this->fontSize/5);
                while ($i > 0) {
                    imagesetpixel($this->img, $px + $i , $py + $i, $color);				
                    $i--;
                }
            }
        }
    }
	/**
	 * 画字符
	 */
	private function printString(){
		//判断前端是否设置字体
		if(isset($_GET['codeFont'])) $this->font = $_GET['codeFont'];
		//判断是否随机字体
		if($this->font == 0 || $this->font > 6){
			$this->font = mt_rand(1,6);
		}
		//构造字体路径
		$font = './font.ttf';
		$x = 0;
		//打印字符到画板
		for($i=0;$i<$this->sum;$i++){
			//设置字体随机颜色
			$color = imagecolorallocate($this->img, rand(30, 150), rand(30, 150), rand(30, 150));
			//计算座标
			$x = mt_rand($this->fontSize*$i*0.95,$this->fontSize*$i*1.1);
			$y = $this->fontSize*1.1;
			//打印字符
			imagettftext($this->img, $this->fontSize, mt_rand(-10, 10), $x, $y, $color, $font, $this->code[$i]);
		}
		
	}
	/**
	 * 创建验证码
	 * @return void
	 */
	private function createCode(){
		//源文本
		$number = "3456789";
		$letter = "zxcvbnmasdfghjklqwertyuioZXCVBNMASDFGHJKLQWERTYUIOP";
		//判断验证码类型
		switch($this->type){
			case 0:
				$codeText = $number;
				break;
			case 1:
				$codeText = $letter;
				break;
			case 2:
				$codeText = $letter.$number;
				break;
			default:
				$codeText = $number;
				break;
		}
		//判断是否自定义字符集合
		if(!is_null($this->str) and $this->str != "") $codeText = $this->str;
		//构造验证码
		$strLen = strlen($codeText);
		$codes = '';
		for($i=0;$i<$this->sum;$i++){
			$this->code[$i] = $codeText{rand(0, $strLen-1)};
			$codes .= $this->code[$i];
		}
		//保存存到session
		@session_start();
		$_SESSION['vcode'] = md5(strtolower($codes));
		// $_SESSION['vcode'] = strtolower($codes);

		$_SESSION['vtime'] = time();
	}
	
	/**
	 * 自动销毁资源
	 */
	function __destruct(){
		@imagedestroy ($this->img);
	}
}
$code = new Code;
$code->getImage();
?>