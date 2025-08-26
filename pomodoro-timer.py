import tkinter as tk
from tkinter import PhotoImage as Pi
import os

class Timer_app:
    def __init__(self):
        self.short_session_seconds = 25*60
        self.short_break_seconds = 5*60
        self.long_session_seconds = 50*60
        self.long_break_seconds = 10*60
        self.timer_id = None
        self.window = tk.Tk()
        self.buttons = []
        self.running = False
        self.short_session_number = 1
        self.short_onbreak = False
        self.long_session_number = 1
        self.long_onbreak = False

    def create_window(self):
        self.window.geometry("600x500")
        self.window.title("Pomodoro Timer")
        self.window.resizable(False,False)

    def create_frames_canvas(self):
        self.menu_frame = tk.Frame(self.window,width=600,height=600)
        self.short_session_frame = tk.Frame(self.window,width=600,height=600)
        self.long_session_frame = tk.Frame(self.window,width=600,height=600)

        self.menu_canvas = tk.Canvas(self.menu_frame,width=600,height=600)
        self.menu_canvas.place(x=0,y=0,relwidth=1,relheight=1)

        self.short_session_canvas = tk.Canvas(self.short_session_frame,width=600,height=600)
        self.short_session_canvas.place(x=0,y=0,relwidth=1,relheight=1)

        self.long_session_canvas = tk.Canvas(self.long_session_frame,width=600,height=600)
        self.long_session_canvas.place(x=0,y=0,relwidth=1,relheight=1)

        self.menu_frame.pack()

    def create_basics_menu(self):
        title = self.menu_canvas.create_text(305,50,font=("Arial",28,"bold"),
                                             text="Pomodoro Timer")

        message = self.menu_canvas.create_text(300,200,font=("Arial",20),
                                               text="Please choose a session to work with")

    def create_buttons(self):
        self.short_button = tk.Button(self.menu_canvas,text="Short Session (25m)",
                                      font=("Arial",12),bg="#B6FABD",
                                      bd=2,activebackground="#B6FABD",
                                      width=20,command=self.switch_to_short)
        self.short_button.place(x=110,y=250)

        self.long_button = tk.Button(self.menu_canvas,text="Long Session (50m)",
                                     font=("Arial",12),bg="#B6FABD",
                                     bd=2,activebackground="#B6FABD",
                                     width=20,command=self.switch_to_long)
        self.long_button.place(x=320,y=250)

        self.exit_button = tk.Button(self.menu_canvas,text="Exit",
                                     font=("Arial",12),bg="#B6FABD",
                                     bd=2,activebackground="#B6FABD",
                                     width=20,command=self.exit)
        self.exit_button.place(x=210,y=295)

        self.short_start_button = tk.Button(self.short_session_canvas,text="Start",
                                            font=("Arial",12),bg="#B6FABD",
                                            bd=2,activebackground="#B6FABD",
                                            width=15,command=self.short_timer_start)
        self.short_start_button.place(x=140,y=260)

        self.short_reset_button = tk.Button(self.short_session_canvas,text="Reset",
                                            font=("Arial",12),bg="#B6FABD",
                                            bd=2,activebackground="#B6FABD",
                                            width=15,command=self.short_reset)
        self.short_reset_button.place(x=320,y=260)

        self.long_start_button = tk.Button(self.long_session_canvas,text="Start",
                                           font=("Arial",12),bg="#B6FABD",
                                           bd=2,activebackground="#B6FABD",
                                           width=15,command=self.long_timer_start)
        self.long_start_button.place(x=140,y=260)

        self.long_reset_button = tk.Button(self.long_session_canvas,text="Reset",
                                           font=("Arial",12),bg="#B6FABD",
                                           bd=2,activebackground="#B6FABD",
                                           width=15,command=self.long_reset)
        self.long_reset_button.place(x=320,y=260)

        self.short_return_to_menu_button = tk.Button(self.short_session_canvas,text="Return To Menu",
                                                     font=("Arial",12),bg="#B6FABD",
                                                     bd=2,activebackground="#B6FABD",
                                                     width=15,command=self.short_return_to_menu)
        self.short_return_to_menu_button.place(x=230,y=310)

        self.long_return_to_menu_button = tk.Button(self.long_session_canvas,text="Return To Menu",
                                                    font=("Arial",12),bg="#B6FABD",
                                                    bd=2,activebackground="#B6FABD",
                                                    width=15,command=self.long_return_to_menu)
        self.long_return_to_menu_button.place(x=230,y=310)

        self.buttons.extend([self.short_button,self.long_button,self.short_start_button,
                             self.short_reset_button,self.short_return_to_menu_button,
                             self.long_start_button,self.long_reset_button,
                             self.long_return_to_menu_button,self.exit_button])
        self.hover_buttons()

    def exit(self):
        self.window.destroy()

    def hover_buttons(self):
        def ligten_color(e):
            e.widget.config(bg="#C7FCCC")
        def darken_color(e):
            e.widget.config(bg="#B6FABD")
        for button in self.buttons:
            button.bind("<Enter>",ligten_color)
            button.bind("<Leave>",darken_color)

    def place_bg(self):
        IMG_PATH = "images"

        self.menu_bg = Pi(file=os.path.join(IMG_PATH,"bg_pink.png"))
        self.short_bg = Pi(file=os.path.join(IMG_PATH,"bg_purple.png"))
        self.long_bg = Pi(file=os.path.join(IMG_PATH,"bg_blue.png"))

        self.menu_canvas.create_image(0,0,anchor="nw",image=self.menu_bg)
        self.short_session_canvas.create_image(0,0,anchor="nw",image=self.short_bg)
        self.long_session_canvas.create_image(0,0,anchor="nw",image=self.long_bg)

    def short_return_to_menu(self):
        self.short_session_frame.pack_forget()
        self.short_reset()
        self.menu_frame.pack()

    def long_return_to_menu(self):
        self.long_session_frame.pack_forget()
        self.long_reset()
        self.menu_frame.pack()

    def switch_to_short(self):
        self.menu_frame.pack_forget()

        self.short_session_frame.pack()

    def switch_to_long(self):
        self.menu_frame.pack_forget()

        self.long_session_frame.pack()
    
    def create_basics_short(self):
        self.short_title = self.short_session_canvas.create_text(295,50,font=("Arial",30,"bold"),text="Session 1")

        self.counter = self.short_session_canvas.create_text(295,200,font=("Arial",35,"bold"),text="25:00")
    
    def create_basics_long(self):
        self.long_title = self.long_session_canvas.create_text(295,50,font=("Arial",30,"bold"),text="Session 1")

        self.counter = self.long_session_canvas.create_text(295,200,font=("Arial",35,"bold"),text="50:00")
        
    def short_timer_start(self):
        if self.short_onbreak:
            self.short_break_timer()
            return
        if not self.running:
            self.short_session_canvas.itemconfig(self.short_title, text=f"Session {self.short_session_number}")
            self.short_session_seconds = 25*60
            self.running = True
            self.short_count_down()
    
    def long_timer_start(self):
        if self.long_onbreak:
            self.long_break_timer()
            return
        if not self.running:
            self.long_session_canvas.itemconfig(self.long_title, text=f"Session {self.long_session_number}")
            self.long_session_seconds = 50*60
            self.running = True
            self.long_count_down()

    def short_break_timer(self):
        if not self.running:
            self.short_session_canvas.itemconfig(self.short_title,text=f"Break {self.short_session_number-1}")
            self.short_break_seconds = 5*60
            self.running = True
            self.short_onbreak = True
            self.short_break_count_down()
    
    def long_break_timer(self):
        if not self.running:
            self.long_session_canvas.itemconfig(self.long_title,text=f"Break {self.long_session_number-1}")
            self.long_break_seconds = 10*60
            self.running = True
            self.long_onbreak = True
            self.long_break_count_down()

    def short_break_count_down(self):
        if self.short_break_seconds <= 0:
            self.running = False
            self.short_onbreak = False
            self.short_timer_start()
            return

        self.short_break_seconds -= 1
        minute = self.short_break_seconds // 60
        second = self.short_break_seconds % 60

        time_label = f"{minute:02}:{second:02}"
        self.short_session_canvas.itemconfig(self.counter,text=time_label)

        self.timer_id = self.window.after(1000,self.short_break_count_down)

    def short_count_down(self):
        if self.short_session_seconds <= 0:
            self.running = False
            self.short_session_number += 1
            self.short_break_timer()
            return
        
        self.short_session_seconds -= 1
        minute = self.short_session_seconds // 60
        second = self.short_session_seconds % 60

        time_label = f"{minute:02}:{second:02}"
        self.short_session_canvas.itemconfig(self.counter,text=time_label)

        self.timer_id = self.window.after(1000,self.short_count_down)

    def long_break_count_down(self):
        if self.long_break_seconds <= 0:
            self.running = False
            self.long_onbreak = False
            self.long_timer_start()
            return

        self.long_break_seconds -= 1
        minute = self.long_break_seconds // 60
        second = self.long_break_seconds % 60

        time_label = f"{minute:02}:{second:02}"
        self.long_session_canvas.itemconfig(self.counter,text=time_label)

        self.timer_id = self.window.after(1000,self.long_break_count_down)

    def long_count_down(self):
        if self.long_session_seconds <= 0:
            self.running = False
            self.long_session_number += 1
            self.long_break_timer()
            return  

        self.long_session_seconds -= 1
        minute = self.long_session_seconds // 60
        second = self.long_session_seconds % 60

        time_label = f"{minute:02}:{second:02}"
        self.long_session_canvas.itemconfig(self.counter,text=time_label)

        self.timer_id = self.window.after(1000,self.long_count_down)

    def short_reset(self):
        if self.running:
            self.window.after_cancel(self.timer_id)
            self.running = False
            if self.short_onbreak:
                self.short_session_canvas.itemconfig(self.counter,text="5:00")
            else:
                self.short_session_canvas.itemconfig(self.counter,text="25:00")
    
    def long_reset(self):
        if self.running:
            self.window.after_cancel(self.timer_id)
            self.running = False
            if self.long_onbreak:
                self.long_session_canvas.itemconfig(self.counter,text="10:00")
            else:
                self.long_session_canvas.itemconfig(self.counter,text="50:00")

app = Timer_app()

app.create_window()
app.create_frames_canvas()
app.place_bg()
app.create_basics_menu()
app.create_basics_short()
app.create_basics_long()
app.create_buttons()

app.window.mainloop()