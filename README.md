# key_registrador
Its a Tool to store Key Strokes, Mouse Moves, Mouse Clicks, Screen shots, Screen Recorders when the user try to do respective actions
### Setup
Required packages for using this tool
1) pynput &nbsp;&nbsp; --> Used to Record Keyboard and Mouse Events
2) smtplib &nbsp;  --> Used to Send Mail
3) opencv&nbsp;&nbsp; --> Used for Screen Recorder
4) Pillow &nbsp; &nbsp; --> Used to take Screen Shots
5) email&nbsp; &nbsp; &nbsp; --> Used to Attach files to Mail (MIMEMultipart)
6) datetime&nbsp;&nbsp; --> Used to get date and time
7) os&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  --> Used to manipulate opertaing systems
8) sys&nbsp; &nbsp; &nbsp; &nbsp; --> Used to manipulate System commands
 
 ## How to use
 ### 1) KeyLogger:
  - python main.py --keylisten --email xxxxx@gmail.com --password xxxxxx --mailduration xxxx(in secs) --stop xxxx(in secs)<br/>
  - python main.py -K -e xxxxx@gmail.com -p xxxxx -D xxxx -S xxxx<br/><br/>
**--keylisten** or **-K**&nbsp; &nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Keyboard Listener (Store Key Strokes)<br/>
