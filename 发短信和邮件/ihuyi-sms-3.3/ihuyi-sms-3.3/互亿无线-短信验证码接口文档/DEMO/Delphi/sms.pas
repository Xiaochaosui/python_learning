//接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
//账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
//注意事项：
//（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
//（2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
//（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

// ************************************************************************ //
// The types declared in this file were generated from data read from the
// WSDL File described below:
// WSDL     : http://106.ihuyi.cn/webservice/sms.php?wsdl
//  >Import : http://106.ihuyi.cn/webservice/sms.php?wsdl:0
// Encoding : utf-8
// Version  : 1.0
// (2013/11/26 10:37:24 - - $Rev: 10138 $)
// ************************************************************************ //

unit sms;

interface

uses InvokeRegistry, SOAPHTTPClient, Types, XSBuiltIns;

const
  IS_OPTN = $0001;
  IS_REF  = $0080;


type

  // ************************************************************************ //
  // The following types, referred to in the WSDL document are not being represented
  // in this file. They are either aliases[@] of other types represented or were referred
  // to but never[!] declared in the document. The types from the latter category
  // typically map to predefined/known XML or Borland types; however, they could also 
  // indicate incorrect WSDL documents that failed to declare or import a schema type.
  // ************************************************************************ //
  // !:int             - "http://www.w3.org/2001/XMLSchema"[Gbl]
  // !:string          - "http://www.w3.org/2001/XMLSchema"[Gbl]
  // !:srting          - "http://www.w3.org/2001/XMLSchema"[Gbl]

  SubmitResult         = class;                 { "http://106.ihuyi.cn/"[GblCplx] }
  ChangePasswordResult = class;                 { "http://106.ihuyi.cn/"[GblCplx] }
  GetNumResult         = class;                 { "http://106.ihuyi.cn/"[GblCplx] }
  VersionInfoResult    = class;                 { "http://106.ihuyi.cn/"[GblCplx] }



  // ************************************************************************ //
  // XML       : SubmitResult, global, <complexType>
  // Namespace : http://106.ihuyi.cn/
  // ************************************************************************ //
  SubmitResult = class(TRemotable)
  private
    Fcode:  Integer;
    Fmsg:   WideString;
    Fsmsid: WideString;
  published
    property code:  Integer     read Fcode write Fcode;
    property msg:   WideString  read Fmsg write Fmsg;
    property smsid: WideString  read Fsmsid write Fsmsid;
  end;



  // ************************************************************************ //
  // XML       : ChangePasswordResult, global, <complexType>
  // Namespace : http://106.ihuyi.cn/
  // ************************************************************************ //
  ChangePasswordResult = class(TRemotable)
  private
    Fcode: Integer;
    Fmsg: WideString;
  published
    property code: Integer     read Fcode write Fcode;
    property msg:  WideString  read Fmsg write Fmsg;
  end;



  // ************************************************************************ //
  // XML       : GetNumResult, global, <complexType>
  // Namespace : http://106.ihuyi.cn/
  // ************************************************************************ //
  GetNumResult = class(TRemotable)
  private
    Fcode: Integer;
    Fmsg: WideString;
    Fnum: Integer;
  published
    property code: Integer     read Fcode write Fcode;
    property msg:  WideString  read Fmsg write Fmsg;
    property num:  Integer     read Fnum write Fnum;
  end;



  // ************************************************************************ //
  // XML       : VersionInfoResult, global, <complexType>
  // Namespace : http://106.ihuyi.cn/
  // ************************************************************************ //
  VersionInfoResult = class(TRemotable)
  private
    Fmsg: WideString;
  published
    property msg: WideString  read Fmsg write Fmsg;
  end;


  // ************************************************************************ //
  // Namespace : http://106.ihuyi.cn/
  // soapAction: http://106.ihuyi.cn/%operationName%
  // transport : http://schemas.xmlsoap.org/soap/http
  // style     : document
  // binding   : smsSoap
  // service   : sms
  // port      : smsSoap
  // URL       : http://106.ihuyi.cn/webservice/sms.php?smsService
  // ************************************************************************ //
  smsSoap = interface(IInvokable)
  ['{228902AE-4B53-39C9-05CA-F389FEE82174}']
    function  Submit(const account: WideString; const password: WideString; const mobile: WideString; const content: WideString): SubmitResult; stdcall;
    function  ChangePassword(const account: WideString; const password: WideString; const newpassword: WideString): ChangePasswordResult; stdcall;
    function  GetNum(const account: WideString; const password: WideString): GetNumResult; stdcall;
    function  VersionInfo: VersionInfoResult; stdcall;
  end;

function GetsmsSoap(UseWSDL: Boolean=System.False; Addr: string=''; HTTPRIO: THTTPRIO = nil): smsSoap;


implementation
  uses SysUtils;

function GetsmsSoap(UseWSDL: Boolean; Addr: string; HTTPRIO: THTTPRIO): smsSoap;
const
  defWSDL = 'http://106.ihuyi.cn/webservice/sms.php?wsdl';
  defURL  = 'http://106.ihuyi.cn/webservice/sms.php?smsService';
  defSvc  = 'sms';
  defPrt  = 'smsSoap';
var
  RIO: THTTPRIO;
begin
  Result := nil;
  if (Addr = '') then
  begin
    if UseWSDL then
      Addr := defWSDL
    else
      Addr := defURL;
  end;
  if HTTPRIO = nil then
    RIO := THTTPRIO.Create(nil)
  else
    RIO := HTTPRIO;
  try
    Result := (RIO as smsSoap);
    if UseWSDL then
    begin
      RIO.WSDLLocation := Addr;
      RIO.Service := defSvc;
      RIO.Port := defPrt;
    end else
      RIO.URL := Addr;
  finally
    if (Result = nil) and (HTTPRIO = nil) then
      RIO.Free;
  end;
end;


initialization
  InvRegistry.RegisterInterface(TypeInfo(smsSoap), 'http://106.ihuyi.cn/', 'utf-8');
  InvRegistry.RegisterDefaultSOAPAction(TypeInfo(smsSoap), 'http://106.ihuyi.cn/%operationName%');
  InvRegistry.RegisterInvokeOptions(TypeInfo(smsSoap), ioDocument);
  RemClassRegistry.RegisterXSClass(SubmitResult, 'http://106.ihuyi.cn/', 'SubmitResult');
  RemClassRegistry.RegisterXSClass(ChangePasswordResult, 'http://106.ihuyi.cn/', 'ChangePasswordResult');
  RemClassRegistry.RegisterXSClass(GetNumResult, 'http://106.ihuyi.cn/', 'GetNumResult');
  RemClassRegistry.RegisterXSClass(VersionInfoResult, 'http://106.ihuyi.cn/', 'VersionInfoResult');

end.