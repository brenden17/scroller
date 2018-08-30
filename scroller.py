import time

try:
    # Python 2
    from Tkinter import Button, Frame, Tk, Label, StringVar, IntVar, Checkbutton, TOP, Y, X, LEFT
except ImportError:
    # Python 3
    from tkinter import Button, Frame, Tk, Label, StringVar, IntVar, Checkbutton, TOP, Y, X, LEFT

import pyautogui

class Scroller:
    def __init__(self, master):

        self.SCROLL_GAP = 400
        self.SCROLL_BIG_GAP = 800

        self.left_scroller_position = (app.winfo_screenwidth()*0.25 , app.winfo_screenheight()/2);
        self.right_scroller_position = (app.winfo_screenwidth()*0.75 , app.winfo_screenheight()/2);

        layer0 = Frame(master)
        layer0.pack(fill=X)

        self.big_gap = IntVar()
        self.big_gap_check_button = Checkbutton(layer0, text="800(a)", variable=self.big_gap)
        self.big_gap_check_button.pack(side=LEFT, padx=25, pady=5)

        self.go_to_up = IntVar()
        self.go_to_up_check_button = Checkbutton(layer0, text="backward(q)", variable=self.go_to_up)
        self.go_to_up_check_button.pack(side=LEFT, padx=1, pady=5)

        layer1 = Frame(master)
        layer1.pack(fill=Y)

        self.left_scroller_label_var = StringVar()
        self.left_scroller_label = Label(layer1, textvariable=self.left_scroller_label_var)
        self.left_scroller_label_var.set(str(self.left_scroller_position))
        self.left_scroller_label.pack(side=TOP, padx=15, pady=5)
        self.left_scroller_button = Button(layer1, text="Set left scroller(1)", command=self.set_left_scroller_position)
        self.left_scroller_button.pack(side=TOP, padx=15, pady=5)

        layer2 = Frame(master)
        layer2.pack(fill=X)

        self.right_scroller_label_var = StringVar()
        self.right_scroller_label = Label(layer2, textvariable=self.right_scroller_label_var)
        self.right_scroller_label_var.set(str(self.right_scroller_position))
        self.right_scroller_label.pack(side=TOP, padx=15, pady=5)
        self.right_scroller_button = Button(layer2, text="Set right scroller(2)", command=self.set_right_scroller_position)
        self.right_scroller_button.pack(side=TOP, padx=5, pady=5)

        master.bind('1', self.set_left_scroller_position)
        master.bind('2', self.set_right_scroller_position)
        
        master.bind('<Up>', self.scroll_up)
        master.bind('<Down>', self.scroll_down)

        master.bind('<Right>', self.scroll_right)
        master.bind('<Left>', self.scroll_left)

        master.bind('<a>', self.toggle_big_gap)
        master.bind('<q>', self.toggle_up_to_go)

        master.bind('<j>', self.scroll_up)
        master.bind('<k>', self.scroll_down)
        master.bind('<h>', self.scroll_left)
        master.bind('<l>', self.scroll_right)

        master.bind("<MouseWheel>", self.mouse_wheel)

    def set_left_scroller_position(self, _event=None):
        self.left_scroller_position = pyautogui.position()
        # print(self.left_scroller_position)
        self.left_scroller_label_var.set(str(self.left_scroller_position))

    def set_right_scroller_position(self, _event=None):
        self.right_scroller_position = pyautogui.position()
        # print(self.right_scroller_position)
        self.right_scroller_label_var.set(str(self.right_scroller_position))

    def mouse_wheel(self, _event):
    # respond to Linux or Windows wheel event
        if _event.num == 5 or _event.delta == -120:
            # self.scrolling(-self.SCROLL_GAP); #down
            self.scroll_down()
        if _event.num == 4 or _event.delta == 120:
            # self.scrolling(self.SCROLL_GAP);
            self.scroll_up()

    def scroll_up(self, _event=None):
        if self.big_gap.get():
            self.scrolling(self.SCROLL_BIG_GAP);
        else:
            self.scrolling(self.SCROLL_GAP);

    def scroll_down(self, _event=None):
        if self.big_gap.get():
            if self.go_to_up.get():
                self.scrolling(self.SCROLL_BIG_GAP);
            else:
                self.scrolling(-self.SCROLL_BIG_GAP);
        else:
            if self.go_to_up.get():
                self.scrolling(self.SCROLL_GAP);
            else:
                self.scrolling(-self.SCROLL_GAP);

    def scroll_right(self, _event=None):
        if self.big_gap.get():
            if self.go_to_up.get():
                self.scrolling(self.SCROLL_BIG_GAP, left=False, right=True);
            else:
                self.scrolling(-self.SCROLL_BIG_GAP, left=False, right=True);
        else:
            if self.go_to_up.get():
                self.scrolling(self.SCROLL_GAP, left=False, right=True);
            else:
                self.scrolling(-self.SCROLL_GAP, left=False, right=True);

    def scroll_left(self, _event=None):
        if self.big_gap.get():
            if self.go_to_up.get():
                self.scrolling(self.SCROLL_BIG_GAP, left=True, right=False);
            else:
                self.scrolling(-self.SCROLL_BIG_GAP, left=True, right=False);
        else:
            if self.go_to_up.get():
                self.scrolling(self.SCROLL_GAP, left=True, right=False);
            else:
                self.scrolling(-self.SCROLL_GAP, left=True, right=False);

    def toggle_big_gap(self, _event=None):
        if self.big_gap.get():
            self.big_gap.set(False)
        else:
            self.big_gap.set(True)

    def toggle_up_to_go(self, _event=None):
        if self.go_to_up.get():
            self.go_to_up.set(False)
        else:
            self.go_to_up.set(True)

    def scrolling(self, scorll_gap, left=True, right=True):
        if left == True:
            pyautogui.click(self.left_scroller_position)
            pyautogui.scroll(scorll_gap)
            time.sleep(0.2)
        if right == True:
            pyautogui.click(self.right_scroller_position)
            pyautogui.scroll(scorll_gap)
            time.sleep(0.2)
        pyautogui.click(app.winfo_x(), app.winfo_y())

app = Tk()

Scroller(app)

app.geometry('%dx%d+%d+%d' % (220, 180, (app.winfo_screenwidth()/2)-110 , app.winfo_screenheight()-250))
app.title("Scroller")
app.lift()
app.attributes("-topmost", True)
app.resizable(0,0)
app.mainloop()
# pyautogui.click((app.winfo_screenwidth()/2)-120 , app.winfo_screenheight()-240)