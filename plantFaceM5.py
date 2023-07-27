from m5stack import *
from m5stack_ui import *
from uiflow import *


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


colorTheme = None
continue2 = None
currentState = None



image0 = M5Img("res/default.png", x=60, y=20, parent=None)
touch_button0 = M5Btn(text='Purple', x=0, y=70, w=150, h=100, bg_c=0xf617c5, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button1 = M5Btn(text='Green', x=163, y=70, w=150, h=100, bg_c=0x17ee6b, text_c=0x000000, font=FONT_MONT_18, parent=None)



def touch_button0_pressed():
  global colorTheme, continue2, currentState
  colorTheme = 'purple'
  touch_button0.set_hidden(True)
  touch_button1.set_hidden(True)
  image0.set_hidden(False)
  currentState = 'dead'
  if currentState == 'happy' and colorTheme == 'purple':
    image0.set_img_src("res/happyface.png")
  if currentState == 'sad' and colorTheme == 'purple':
    image0.set_img_src("res/purplemad.png")
  if currentState == 'dead' and colorTheme == 'purple':
    image0.set_img_src("res/purpledead.png")
  pass
touch_button0.pressed(touch_button0_pressed)

def touch_button1_pressed():
  global colorTheme, continue2, currentState
  colorTheme = 'green'
  touch_button0.set_hidden(True)
  touch_button1.set_hidden(True)
  image0.set_hidden(False)
  currentState = 'dead'
  if currentState == 'happy' and colorTheme == 'green':
    image0.set_img_src("res/greenhappy.png")
  if currentState == 'sad' and colorTheme == 'green':
    image0.set_img_src("res/sadface.png")
  if currentState == 'dead' and colorTheme == 'green':
    image0.set_img_src("res/greendead.png")
  pass
touch_button1.pressed(touch_button1_pressed)


continue2 = 0
image0.set_hidden(True)
