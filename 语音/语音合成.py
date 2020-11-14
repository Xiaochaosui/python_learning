# 系统客户端
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Speak("xcs is a good man")