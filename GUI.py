from tkinter import *
import PIL.Image as image
import PIL.ImageDraw as imageDraw
from Cnn import Cnn
import string

class GUI:

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'white'

    def __init__(self):
        self.root = Tk()
        self.cnn = Cnn('modelloSwag.dat')
        self.c = Canvas(self.root, bg='black', width=600, height=600)
        self.image = image.new("RGB", (600, 600), (0, 0, 0))
        self.draw = imageDraw.Draw(self.image)
        self.c.grid(row=1, columnspan=5)
        save_button = Button(self.root, text='clear', command=lambda : self.c.create_rectangle(0,0,600,600,fill='black'))
        save_button.grid(row=0, column=2)
        save_button = Button(self.root, text='guess', command=lambda : self.writePrediction())
        save_button.grid(row=0, column=1)
        self.labelText = StringVar()
        self.t = Label(self.root, textvariable = self.labelText).grid(row=0)
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.DEFAULT_PEN_SIZE
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
    
    def writePrediction(self):
        self.labelText.set(self.cnn.getPredict(self.getImage()))
        print(self.cnn.getPredict(self.getImage()))
    
    def paint(self, event):
        self.line_width = self.DEFAULT_PEN_SIZE
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=(255,255,255), width=5)
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=paint_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None,  None

    def getImage(self):
        return self.image