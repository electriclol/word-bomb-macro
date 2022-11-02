print('''".u" to undo, ".l" to set the letters, ".a" to add letters''')
alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabet.split()
import pyperclip
import random
import pyautogui as pag
import time
time.sleep(5)
blanklist = []
words = open("words.txt").read()
undolist = []
words = words.split()
wcounter = -1
for x in words:
  wcounter = wcounter + 1
  words[wcounter] = words[wcounter].lower()
while True:
  counter = 0
  pag.click(960, 1026)
  pag.click(960, 1026)
  pag.click(960, 1026)
  pag.hotkey('ctrl', 'c')
  pag.click(960, 700)
  if "is up" in pyperclip.paste():
    ""
  else:
    if len(alphabet) == 0:
      alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
      alphabet = alphabet.split()
    pag.click(960, 540)
    pag.click(960, 540)
    pag.hotkey('ctrl', 'c')
    pag.click(960, 700)
    wordstart = pyperclip.paste().lower()
    anothercounter = 0
    max = 0
    biggestword = ""
    for x in words:
        if wordstart in x:
            fakealphabet = alphabet.copy()
            for letter in x:
                if letter in fakealphabet:
                    anothercounter = anothercounter + 1
                    fakealphabet.remove(letter)
            if anothercounter >= max:
                max = anothercounter
                biggestword = x
        anothercounter = 0
    pag.write(biggestword, interval = 0.05)
    pag.press('enter')
    words.remove(biggestword)
    undolist = []
    for bwletter in biggestword:
        try:
            alphabet.remove(bwletter)
            undolist.append(bwletter)
        except:
            ""
  pyperclip.copy("")
