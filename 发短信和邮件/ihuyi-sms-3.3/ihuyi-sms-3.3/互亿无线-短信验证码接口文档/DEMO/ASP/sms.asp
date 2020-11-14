<%@LANGUAGE="VBSCRIPT" CODEPAGE="936"%>
<%

 '接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
 '账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
 '注意事项：
 '（1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。；
 '（2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及APIkey来调用接口；
 '（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

Response.Charset = "gb2312"

'<meta http-equiv="Content-Type" content="text/html; charset=gbk" />

'asp UTF转GB2312   将UTF8编码文字转换为GB编码文字的asp代码
function UTF2GB(UTFStr)
for Dig=1 to len(UTFStr)
   '如果UTF8编码文字以%开头则进行转换
   if mid(UTFStr,Dig,1)="%" then
      'UTF8编码文字大于8则转换为汉字
     if len(UTFStr) >= Dig+8 then
        GBStr=GBStr & ConvChinese(mid(UTFStr,Dig,9))
        Dig=Dig+8
     else
       GBStr=GBStr & mid(UTFStr,Dig,1)
     end if
   else
      GBStr=GBStr & mid(UTFStr,Dig,1)
   end if
next
UTF2GB=GBStr
end function

'GB2312转UTF8的asp代码  将GB编码文字转换为UTF8编码文字
Function toUTF8(szInput)
     Dim wch, uch, szRet
     Dim x
     Dim nAsc, nAsc2, nAsc3
     '如果输入参数为空，则退出函数
     If szInput = "" Then
         toUTF8 = szInput
         Exit Function
     End If
     '开始转换
      For x = 1 To Len(szInput)
         '利用mid函数分拆GB编码文字
         wch = Mid(szInput, x, 1)
         '利用ascW函数返回每一个GB编码文字的Unicode字符代码
         '注：asc函数返回的是ANSI 字符代码，注意区别
         nAsc = AscW(wch)
         If nAsc < 0 Then nAsc = nAsc + 65536
    
         If (nAsc And &HFF80) = 0 Then
             szRet = szRet & wch
         Else
             If (nAsc And &HF000) = 0 Then
                 uch = "%" & Hex(((nAsc \ 2 ^ 6)) Or &HC0) & Hex(nAsc And &H3F Or &H80)
                 szRet = szRet & uch
             Else
                'GB编码文字的Unicode字符代码在0800 - FFFF之间采用三字节模版
                 uch = "%" & Hex((nAsc \ 2 ^ 12) Or &HE0) & "%" & _
                             Hex((nAsc \ 2 ^ 6) And &H3F Or &H80) & "%" & _
                             Hex(nAsc And &H3F Or &H80)
                 szRet = szRet & uch
             End If
         End If
     Next         
     toUTF8 = szRet
End Function

'二进制转换为十六进制的asp代码
function c2to16(x)
    i=1
    for i=1 to len(x) step 4
       c2to16=c2to16 & hex(c2to10(mid(x,i,4)))
    next
end function

'二进制转换为十进制的asp代码
function c2to10(x)
    c2to10=0
    if x="0" then exit function
      i=0
    for i= 0 to len(x) -1
       if mid(x,len(x)-i,1)="1" then c2to10=c2to10+2^(i)
    next
end function

'十六进制转换为二进制的asp代码
function c16to2(x)
     i=0
     for i=1 to len(trim(x))
       tempstr= c10to2(cint(int("&h" & mid(x,i,1))))
       do while len(tempstr)<4
          tempstr="0" & tempstr
       loop
       c16to2=c16to2 & tempstr
    next
end function

function c10to2(x)
    mysign=sgn(x)
    x=abs(x)
    DigS=1
    do
       if x<2^DigS then
         exit do
       else
         DigS=DigS+1
       end if
    loop
    tempnum=x
    i=0
    for i=DigS to 1 step-1
       if tempnum>=2^(i-1) then
          tempnum=tempnum-2^(i-1)
          c10to2=c10to2 & "1"
       else
          c10to2=c10to2 & "0"
       end if
    next
    if mysign=-1 then c10to2="-" & c10to2
end function

'UTF8编码文字将转换为汉字
function ConvChinese(x)
    A=split(mid(x,2),"%")
    i=0
    j=0
   for i=0 to ubound(A)
      A(i)=c16to2(A(i))
   next
   for i=0 to ubound(A)-1
     DigS=instr(A(i),"0")
     Unicode=""
     for j=1 to DigS-1
       if j=1 then
         A(i)=right(A(i),len(A(i))-DigS)
         Unicode=Unicode & A(i)
       else
          i=i+1
          A(i)=right(A(i),len(A(i))-2)
          Unicode=Unicode & A(i)
       end if
     next
     if len(c2to16(Unicode))=4 then
        ConvChinese=ConvChinese & chrw(int("&H" & c2to16(Unicode)))
     else
        ConvChinese=ConvChinese & chr(int("&H" & c2to16(Unicode)))
     end if
   next
end function

'GB2312中文转unicode(&#)的asp代码  将GB编码文字转换为unicode编码文字
function chinese2unicode(Str)
   dim i
   dim Str_one
   dim Str_unicode
   if(isnull(Str)) then
      exit function
   end if
   for i=1 to len(Str)
     Str_one=Mid(Str,i,1)
     Str_unicode=Str_unicode&chr(38)
     Str_unicode=Str_unicode&chr(35)
     Str_unicode=Str_unicode&chr(120)
     Str_unicode=Str_unicode& Hex(ascw(Str_one))
     Str_unicode=Str_unicode&chr(59)
   next
   chinese2unicode=Str_unicode
end function  

'URL地址编码解码函数
Function URLDecode(enStr)
dim deStr
dim c,i,v
deStr=""
for i=1 to len(enStr)
   c=Mid(enStr,i,1)
   if c="%" then
    v=eval("&h"+Mid(enStr,i+1,2))
    if v<128 then
     deStr=deStr&chr(v)
     i=i+2
    else
     if isvalidhex(mid(enstr,i,3)) then
      if isvalidhex(mid(enstr,i+3,3)) then
       v=eval("&h"+Mid(enStr,i+1,2)+Mid(enStr,i+4,2))
       deStr=deStr&chr(v)
       i=i+5
      else
       v=eval("&h"+Mid(enStr,i+1,2)+cstr(hex(asc(Mid(enStr,i+3,1)))))
       deStr=deStr&chr(v)
       i=i+3
      end if
     else
      destr=destr&c
     end if
    end if
   else
    if c="+" then
     deStr=deStr&" "
    else
     deStr=deStr&c
    end if
   end if
next
URLDecode=deStr
end function

'判断是否为有效的十六进制代码
function isvalidhex(str)
dim c
isvalidhex=true
str=ucase(str)
if len(str)<>3 then isvalidhex=false:exit function
if left(str,1)<>"%" then isvalidhex=false:exit function
   c=mid(str,2,1)
if not (((c>="0") and (c<="9")) or ((c>="A") and (c<="Z"))) then isvalidhex=false:exit function
   c=mid(str,3,1)
if not (((c>="0") and (c<="9")) or ((c>="A") and (c<="Z"))) then isvalidhex=false:exit function
end Function



'请求数据到短信接口
Function Post(url,data)
	dim Https
	set Https=server.createobject("MSXML2.XMLHTTP")
	Https.open "POST",url,false
	Https.setRequestHeader "Content-Type","application/x-www-form-urlencoded"
	Https.send data
	if Https.readystate=4 then
		dim objstream
		set objstream = Server.CreateObject("adodb.stream")
		objstream.Type = 1
		objstream.Mode =3
		objstream.Open
		objstream.Write Https.responseBody
		objstream.Position = 0
		objstream.Type = 2
		objstream.Charset = "utf-8"
		Post = objstream.ReadText
		objstream.Close
		set objstream = nothing
		set https=nothing
	end if
End Function

'函数返回随机整数。
Function gen_key(digits)	
	'Create and define array
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
	
	'Initiate randomize method for default seeding
	randomize
	
	'Loop through and create the output based on the the variable passed to
	'the function for the length of the key.
	do while len(output) < digits
	num = char_array(Int((9 - 0 + 1) * Rnd + 0))
	output = output + num
	loop
	
	'Set return
	gen_key = output
End Function


Dim mobile
mobile = request("mobile")	'登录用户名


    if mobile="" then
       response.Write("手机号码不能为空")
    else
	if trim(session("validateCode")) <> trim(Request("send_code")) then
		response.write("请输入正确的验证码")
		response.end
	else
			dim target,post_data,content,res,mobile_code
			mobile_code = gen_key(4)
			Session("mobile_code") = mobile_code
			'Response.Cookies("mobile_code") = mobile_code
			Session("mobile") = mobile
			'Response.Cookies("mobile") = mobile
			target = "http://106.ihuyi.cn/webservice/sms.php?method=Submit"
			content = toUTF8("您的验证码是："&mobile_code&"。请不要把验证码泄露给其他人。")
			post_data = "account=用户名&password=密码&mobile="&mobile&"&content="&content
			'查看用户名请登录用户中心->验证码短信->产品总览->APIID
			'查看密码请登录用户中心->验证码短信->产品总览->APIKEY
			'Response.write toUTF8("短信测试")
			'response.Write(UTF2GB(Post(target,post_data)))
	
			tempstr = UTF2GB(Post(target,post_data))
			'if instr(tempstr,"提交成功")>0 Then
				'response.Write("true") 
			'else
				'response.Write("error") 
			'end if
	
			Dim len1,len2
			len1 = instr(1,tempstr,"</code>",1)-1
			len2 = instr(1,tempstr,"<code>",1)
			'response.Write(len2)
			code=left(tempstr,len1)
			code=right(code,(len1-len2-5))
			'response.Write(code)
	
			Dim len3,len4
			len3 = instr(1,tempstr,"</msg>",1)-1
			len4 = instr(1,tempstr,"<msg>",1)
			'response.Write(len2)
			msg=left(tempstr,len3)
			msg=right(msg,(len3-len4-4))
			response.Write(msg)
			
		end if

    end If
%>