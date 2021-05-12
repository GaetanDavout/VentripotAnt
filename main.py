#                                 \
#                 .___             `.
#    ___              `~\           |               \
#  o~   `.               |         /'                |
#.----._ `|             ,'       /'              _./'
#`o     `\|___       __,|----'~~~~T-----,__  _,'~
#      /~~o   `~>-/|~ '   ' ,   '      '   ~~\_
#     |_      <~   |   ' ,   ' '   '  ' , '     \
#       `-...-'~\./' '     '     '   '   '  , '  >
#                 `-, __'  ,  '  '  , ' ,   '_,'-'
#                   /'   `~~~~~~~|`--------~~\
#                 /'            ,'            `.
#          ~~`---'             /               |
#                           ,-'              _/'
#
#______________________________________________________________
#
#                    VentripotAnt v0.0.1
#              Arthur PALDINO - Gaetan DAVOUT
#
# Avancement :
# - Projet : #--------- 0.1%
#


import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

x = 1024
y = 768
Fourmilliere = np.zeros((x, y), np.int8)

if __name__ == '__main__':
    window = tk.Tk()
    #greeting = tk.Label(text="Hello, VentripotAnt !")
    #greeting.pack()
    img = ImageTk.PhotoImage(image=Image.fromarray(Fourmilliere))
    canvas = tk.Canvas(window, width=x, height=y)
    canvas.pack()
    canvas.create_image(20, 20, anchor="nw", image=img)

    window.mainloop()

