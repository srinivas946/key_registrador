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
 
### List of Commands
**--Keylisten** (or) **-K**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Initiate the Keyboard Listener(Store Key logs)<br/>
**--mouselisten** (or) **-M**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;-->&nbsp; &nbsp; &nbsp; Initiate the Mouse Listener(Strore Mouse Actions)<br/>
**--keymouserlisten** (or) **-L**&nbsp; &nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Initiate both Keyboard and Mouse Listener<br/>
**--recordscreen** (or) **-r**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Initiate Screen Recorder<br/>
**--keymousescrnrec** (or) **-R**&nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Initiate Keyboard, Mouse, Screen Recorder<br/>
**--capture** (or) **-c**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Screen Capture (set to True or False)<br/>
**--capturetime** (or) **-t**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Set the Screen Recorder time (in secs)<br/>
**--email** (or) **-e**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -->&nbsp; &nbsp; &nbsp; Enter Users Gmail ID<br/>
**--password** (or) **-p**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;-->&nbsp; &nbsp; &nbsp; Enter Gmail Password<br/>
**--fps** (or) **-F**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> &nbsp; &nbsp; &nbsp; Frames Per Second<br/>
**--mailduration** (or) **-D**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> &nbsp; &nbsp; &nbsp; Duration of Mail send to the User<br/>
**--stop** (or) **-S**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> &nbsp; &nbsp; &nbsp; Stops the Program Execution based on given time (in secs)<br/>

## How to use
### 1) keylogger
- python&nbsp; main.py&nbsp; --keylisten&nbsp; --email&nbsp; xxxxxxxx&nbsp; --password&nbsp; xxxxxx&nbsp; --mailduration&nbsp; xxx &nbsp; --stop&nbsp; xxx<br/>
- python&nbsp; main.py&nbsp; -K&nbsp; -e&nbsp; xxxxxxx&nbsp; -p&nbsp; xxxxxx&nbsp; -D&nbsp; xxx&nbsp; -S&nbsp; xxx<br/>

### 2) Mouselogger
- python&nbsp; main.py&nbsp; --mouselisten&nbsp; --email&nbsp; xxxxx&nbsp; --password&nbsp; xxxx&nbsp; --mailduraiton&nbsp; xxx&nbsp; --stop&nbsp; xxx<br/>
- python&nbsp; main.py&nbsp; -M&nbsp; -e&nbsp; xxxxxxx&nbsp; -p&nbsp; xxxxx&nbsp; -D&nbsp; xxxx&nbsp; -S&nbsp; xxxx<br/>

### 3) KeymouseLogger
- python&nbsp; main.py&nbsp; --keymouselisten&nbsp; --email&nbsp; xxxxxxxxx&nbsp; --password&nbsp; xxxxxxxx&nbsp; --mailduration&nbsp; xxx&nbsp; --stop&nbsp; xxx<br/>
- python&nbsp; main.py&nbsp; -L&nbsp; -e&nbsp; xxxxxxxxxx&nbsp; -p&nbsp; xxxxxxxx&nbsp; -D&nbsp; xxxx&nbsp; -S&nbsp; xxxxx<br/>
### 4) KeymouseLogger with Screen shots
- python&nbsp; main.py&nbsp; --keymouserlisten&nbsp; --email&nbsp; xxxxxxxx&nbsp; --password&nbsp; xxxxxxx&nbsp; --mailduration&nbsp; xxxx&nbsp; --capture&nbsp; --stop&nbsp; xxxxx<br/>
- python&nbsp; main.py&nbsp; -L&nbsp; -e&nbsp; xxxxxxx&nbsp; -p&nbsp; xxxxxxx&nbsp; -D xxxx&nbsp; -c&nbsp; -S&nbsp; xxxx<br/>

### 5) Screen Recorder
- python&nbsp; main.py&nbsp; --recordscreen&nbsp; --email&nbsp; xxxxxxxx&nbsp; --password&nbsp; xxxxxxxxx&nbsp; --capturetime&nbsp; xxxx&nbsp; --fps&nbsp; xxxxx<br/>
- python&nbsp; main.py&nbsp; -r&nbsp; -e&nbsp; xxxxxxxxx&nbsp; -p&nbsp; xxxxxxx&nbsp; -t&nbsp; xxxx&nbsp; -F&nbsp; xxxx<br/>

### 6) KeymouseLogger with Screen Recorder
- python&nbsp; main.py&nbsp; --keymousescrnrec&nbsp; --email&nbsp; xxxxxx&nbsp; --password&nbsp; xxxxxxx&nbsp; --mailduration&nbsp; xxxxxx&nbsp; --capturetime&nbsp; xxxx&nbsp; --fps&nbsp; xxxx&nbsp; --stop&nbsp; xxxxxx&nbsp;<br/>
- python&nbsp; main.py&nbsp; -R&nbsp; -e&nbsp; xxxxxxx&nbsp; -p&nbsp; xxxxxx&nbsp; -D&nbsp; xxxxx&nbsp; -t&nbsp; xxxxx&nbsp; -F&nbsp; xxxx&nbsp; -S&nbsp; xxxx<br/>

### 7) KeymouseLogger with Screen Recorder and Screen Shots
- python&nbsp; main.py&nbsp; --keymousescrnrec&nbsp; --email&nbsp; xxxxxxxxxx&nbsp; --password&nbsp; xxxxxxx&nbsp; --mailduration&nbsp; xxxx&nbsp; --capturetime&nbsp; xxxx&nbsp; --fps&nbsp; xxxxx&nbsp; --capture&nbsp; --stop&nbsp; xxxx<br/>
- python&nbsp; main.py&nbsp; -R&nbsp; -e&nbsp; xxxxxxx&nbsp; -p&nbsp; xxxxx&nbsp; -D&nbsp; xxxxxxx&nbsp; -t&nbsp; xxxxxx&nbsp; -F&nbsp; xxxx&nbsp; -c&nbsp; -S&nbsp; xxxxx<br/>

## Note:
- Using this tool you can get the logs from keyboard, mouse and also take screen shots, Screen Recorder and send the details to the mail provided by the user at run time<br/>
- Screen Shots are captured based on the keywords, external KeywordFile.txt is provided to add the keywords<br/>
- Use less value for FPS (Frames Per Second) in screen recording. If you provided more fps, it will consume more memory and delay in sending mail to user (consume more memory and internet)

## Kind Request:
This tool is desined only for gaining knowledge/awareness on how keyloggers work in real time. So its my kind request, do not use it for illegal purposes
