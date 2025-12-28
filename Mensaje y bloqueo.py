import time, usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_win_es import KeyboardLayout

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd) 

time.sleep(5) # Delay de seguridad

kbd.press(Keycode.GUI, Keycode.R)
kbd.release_all()
time.sleep(0.5)

layout.write("cmd /c \"echo. > %temp%\\note.txt && notepad %temp%\\note.txt\"") 
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(1.5) # Esperar a que el sistema procese y abra

# --- INGRESE SU MENSAJE AQUÍ ---
layout.write("GRACIAS POR PERMITIR MI ACCESO, TODA TU INFORMACION FUE ROBADA :)")
time.sleep(3.0)
kbd.press(Keycode.GUI,Keycode.L)
kbd.release_all()
