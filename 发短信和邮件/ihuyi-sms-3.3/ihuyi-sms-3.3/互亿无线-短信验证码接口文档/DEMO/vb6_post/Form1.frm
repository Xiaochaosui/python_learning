VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   9285
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   18105
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   9285
   ScaleWidth      =   18105
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command2 
      Caption         =   "自动提交"
      Height          =   495
      Left            =   3840
      TabIndex        =   7
      Top             =   8520
      Width           =   1575
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   1000
      Left            =   2640
      Top             =   240
   End
   Begin VB.TextBox content 
      Height          =   375
      Left            =   1080
      TabIndex        =   6
      Top             =   840
      Width           =   16575
   End
   Begin VB.TextBox mobile 
      Height          =   375
      Left            =   1080
      TabIndex        =   4
      Top             =   240
      Width           =   1215
   End
   Begin VB.CommandButton Command3 
      Caption         =   "语音通知"
      Height          =   495
      Left            =   2160
      TabIndex        =   2
      Top             =   8520
      Width           =   1335
   End
   Begin VB.CommandButton Command1 
      Caption         =   "发送短信"
      Height          =   495
      Left            =   480
      TabIndex        =   1
      Top             =   8520
      Width           =   1455
   End
   Begin VB.TextBox Text2 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000001&
      Height          =   6615
      Left            =   480
      Locked          =   -1  'True
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   0
      Top             =   1440
      Width           =   17295
   End
   Begin VB.Label Label2 
      Caption         =   "内容"
      Height          =   255
      Left            =   480
      TabIndex        =   5
      Top             =   960
      Width           =   855
   End
   Begin VB.Label Label1 
      Caption         =   "手机"
      Height          =   255
      Left            =   480
      TabIndex        =   3
      Top             =   360
      Width           =   735
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim HttpClient As Object
Dim rndstr
Private Declare Function timeGetTime Lib "winmm.dll" () As Long

Sub Send(TypeB As Boolean)
    Dim account$, password$, url$, postData$
    
    If TypeB Then
        url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"           '这个是短信地址
        account = "test"
        password = "test"
    Else
        url = "http://api.vm.ihuyi.com/webservice/voice.php?method=Submit"      '这个是电话的地址
        account = "test"
        password = "test"
    End If

    postData = "account=" & account & "&password=" & password & "&mobile=" & mobile & "&content=" & content
    
    Set HttpClient = CreateObject("Microsoft.XMLHTTP")
    HttpClient.open "POST", url, False
    HttpClient.setRequestHeader "CONTENT-TYPE", "application/x-www-form-urlencoded"
    HttpClient.setRequestHeader "Content-Length", Len(postData)
    
    HttpClient.Send UTF8EncodeURI(postData)
    
    Do While HttpClient.readyState <> 4
        DoEvents
    Loop
    
    Text2.Text = Text2.Text & vbCrLf & Time$ & " " & Right(timeGetTime, 3) & " " & HttpClient.responseText
    
End Sub

Private Sub Command1_Click()
    Send True
End Sub

Private Sub Command3_Click()
    Send False
End Sub

Private Sub Form_Load()
    rndstr = 1213412
    content.Text = "您的验证码是：" & rndstr & "。请不要把验证码泄露给其他人。"
End Sub

Private Sub Timer1_Timer()
    Dim rndstr2
    rndstr2 = Int(Rnd * 9000)
    content.Text = Replace(content.Text, rndstr, rndstr2)
    rndstr = rndstr2
    Text2.Text = Text2.Text & vbCrLf & Time$ & " " & Right(timeGetTime, 3)
    Command1_Click
    Command3_Click
End Sub

Private Sub Command2_Click()
    If Timer1.Enabled = False Then
        Timer1.Enabled = True
        Command2.Caption = "自动提交（关）"
    ElseIf Timer1.Enabled = True Then
        Timer1.Enabled = False
        Command2.Caption = "自动提交（开）"
    End If
End Sub


Function UTF8EncodeURI(szInput)
    Dim wch, uch, szRet
    Dim x
    Dim nAsc, nAsc2, nAsc3
    If szInput = "" Then
        UTF8EncodeURI = szInput
        Exit Function
    End If
    For x = 1 To Len(szInput)
        wch = Mid(szInput, x, 1)
        nAsc = AscW(wch)
        If nAsc < 0 Then nAsc = nAsc + 65536
        If (nAsc And &HFF80) = 0 Then
            szRet = szRet & wch
        Else
            If (nAsc And &HF000) = 0 Then
                uch = "%" & Hex(((nAsc \ 2 ^ 6)) Or &HC0) & Hex(nAsc And &H3F Or &H80)
                szRet = szRet & uch
            Else
                uch = "%" & Hex((nAsc \ 2 ^ 12) Or &HE0) & "%" & _
                Hex((nAsc \ 2 ^ 6) And &H3F Or &H80) & "%" & _
                Hex(nAsc And &H3F Or &H80)
                szRet = szRet & uch
            End If
        End If
    Next
    UTF8EncodeURI = szRet
End Function

Function GBKEncodeURI(szInput)
    Dim i As Long
    Dim x() As Byte
    Dim szRet As String
    szRet = ""
    x = StrConv(szInput, vbFromUnicode)
    For i = LBound(x) To UBound(x)
        szRet = szRet & "%" & Hex(x(i))
    Next
    GBKEncodeURI = szRet
End Function

