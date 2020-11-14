//接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
//账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
//注意事项：
//（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
//（2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
//（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

using System;
using System.Data;
using System.Configuration;
using System.Collections;
using System.IO;
using System.Net;
using System.Text;
using System.Web;
using System.Web.Security;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;

public partial class Post : System.Web.UI.Page
{
    public static string PostUrl = ConfigurationManager.AppSettings["WebReference.Service.PostUrl"];
    protected void Page_Load(object sender, EventArgs e)
    {
        string account = "用户名";//用户名是登录用户中心->验证码、通知短信->帐户及签名设置->APIID
        string password = "密码"; //密码是请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
        string mobile = Request.QueryString["mobile"];
		Random rad = new Random();
        int mobile_code = rad.Next(1000, 10000);
        string content = "您的验证码是：" + mobile_code + " 。请不要把验证码泄露给其他人。";
		
		//Session["mobile"] = mobile;
		//Session["mobile_code"] = mobile_code;
        
		string postStrTpl = "account={0}&password={1}&mobile={2}&content={3}";

        UTF8Encoding encoding = new UTF8Encoding();
        byte[] postData = encoding.GetBytes(string.Format(postStrTpl, account, password, mobile, content));

        HttpWebRequest myRequest = (HttpWebRequest)WebRequest.Create(PostUrl);
        myRequest.Method = "POST";
        myRequest.ContentType = "application/x-www-form-urlencoded";
        myRequest.ContentLength = postData.Length;

        Stream newStream = myRequest.GetRequestStream();
        // Send the data.
        newStream.Write(postData, 0, postData.Length);
        newStream.Flush();
        newStream.Close();

        HttpWebResponse myResponse = (HttpWebResponse)myRequest.GetResponse();
        if (myResponse.StatusCode == HttpStatusCode.OK)
        {
            StreamReader reader = new StreamReader(myResponse.GetResponseStream(), Encoding.UTF8);

               //Response.Write(reader.ReadToEnd());

               string res = reader.ReadToEnd();
               int len1 = res.IndexOf("</code>");
               int len2 = res.IndexOf("<code>");
               string code=res.Substring((len2+6),(len1-len2-6));
               //Response.Write(code);

               int len3 = res.IndexOf("</msg>");
               int len4 = res.IndexOf("<msg>");
               string msg=res.Substring((len4+5),(len3-len4-5));
               Response.Write(msg);

               Response.End();

        }
        else
        {
            //访问失败
        }
    }
}
