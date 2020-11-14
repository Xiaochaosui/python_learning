unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    procedure Button1Click(Sender: TObject);

  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

uses sms;

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
var ts:SubmitResult;

begin
      ts:=sms.GetsmsSoap(true).Submit(Edit1.Text,Edit2.Text,Edit3.Text,Memo1.Text);
      ShowMessage(inttostr(ts.code) + ' - ' + ts.msg);
      Edit4.Text:=inttostr(ts.code) + ' - ' + ts.msg;
end;


end.
