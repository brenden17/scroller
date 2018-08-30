import time

try:
    # Python 2
    from Tkinter import Button, Frame, Tk, Label, StringVar, IntVar, Checkbutton, TOP, Y, X, LEFT, RIGHT
except ImportError:
    # Python 3
    from tkinter import Button, Frame, Tk, Label, StringVar, IntVar, Checkbutton, TOP, Y, X, LEFT, RIGHT

import pyautogui

class Scroller:
    def __init__(self, master):

        self.SCROLL_GAP = 20
        self.SCROLL_BIG_GAP = 100

        self.left_scroller_position = (app.winfo_screenwidth()*0.25 , app.winfo_screenheight()/2);
        self.right_scroller_position = (app.winfo_screenwidth()*0.75 , app.winfo_screenheight()/2);

        layer0 = Frame(master)
        layer0.pack(fill=X)

        self.go_to_up = IntVar()
        self.go_to_up_check_button = Checkbutton(layer0, text="Backward [1]", variable=self.go_to_up)
        self.go_to_up_check_button.pack(side=LEFT, padx=1, pady=5)

        self.focus_left = IntVar()
        self.focus_left_check_button = Checkbutton(layer0, text="Focus on left [2]", variable=self.focus_left)
        self.focus_left_check_button.pack(side=LEFT, padx=25, pady=5)

        self.focus_right = IntVar()
        self.focus_right_check_button = Checkbutton(layer0, text="Focus on right [3]", variable=self.focus_right)
        self.focus_right_check_button.pack(side=LEFT, padx=25, pady=5)
        
        self.big_gap = IntVar()
        self.big_gap_check_button = Checkbutton(layer0, text="100 [4]", variable=self.big_gap)
        self.big_gap_check_button.pack(side=LEFT, padx=25, pady=5)

        # layer1 = Frame(master)
        # layer1.pack(fill=Y)

        self.right_scroller_label_var = StringVar()
        self.right_scroller_label = Label(layer0, textvariable=self.right_scroller_label_var)
        self.right_scroller_label_var.set(str(self.right_scroller_position))
        self.right_scroller_label.pack(side=RIGHT, padx=15, pady=5)

        self.left_scroller_label_var = StringVar()
        self.left_scroller_label = Label(layer0, textvariable=self.left_scroller_label_var)
        self.left_scroller_label_var.set(str(self.left_scroller_position))
        self.left_scroller_label.pack(side=RIGHT, padx=15, pady=5)
        # self.left_scroller_button = Button(layer0, text="Set left scroller(8)", command=self.set_left_scroller_position)
        # self.left_scroller_button.pack(side=RIGHT, padx=15, pady=5)

        # layer2 = Frame(master)
        # layer2.pack(fill=X)

        # self.right_scroller_button = Button(layer0, text="Set right scroller(9)", command=self.set_right_scroller_position)
        # self.right_scroller_button.pack(side=RIGHT, padx=5, pady=5)

        master.bind('8', self.set_left_scroller_position)
        master.bind('9', self.set_right_scroller_position)
        
        master.bind('<Up>', self.scroll_up)
        master.bind('<Down>', self.scroll_down)

        master.bind('<Right>', self.scroll_right)
        master.bind('<Left>', self.scroll_left)

        master.bind('1', self.toggle_up_to_go)
        master.bind('2', self.toggle_focus_left)
        master.bind('3', self.toggle_focus_righ)
        master.bind('4', self.toggle_big_gap)

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

    def toggle_focus_left(self, _event=None):
        pyautogui.click(self.left_scroller_position)

    def toggle_focus_righ(self, _event=None):
        pyautogui.click(self.right_scroller_position)

    def scrolling(self, scorll_gap, left=True, right=True):
        if left == True:
            pyautogui.click(self.left_scroller_position)
            pyautogui.scroll(scorll_gap)
            # time.sleep(0.2)
        if right == True:
            pyautogui.click(self.right_scroller_position)
            pyautogui.scroll(scorll_gap)
            # time.sleep(0.2)
        pyautogui.click(app.winfo_screenwidth()-200, app.winfo_y()+30)

app = Tk()

Scroller(app)

app.geometry('%dx%d+%d+%d' % (app.winfo_screenwidth(), 40, (app.winfo_screenwidth()/2)-110 , app.winfo_screenheight()-40))
app.title("Scroller")
app.lift()
app.attributes("-topmost", True)
app.resizable(0,0)
app.mainloop()
# pyautogui.click((app.winfo_screenwidth()/2)-120 , app.winfo_screenheight()-240)