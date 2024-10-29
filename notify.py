from notifypy import Notify

try:
    notification = Notify()
    notification.title = "Taks complete"
    notification.message = "All images was converted"
    notification.icon = './assets/images/icon-art.png'
    notification.audio = "./assets/sound/uwu.wav"
    notification.send()
except:
    print('No se ejecuto el sonido')