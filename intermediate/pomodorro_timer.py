import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
CHECKS = "✔️"

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global REPS 
    REPS = 0
    window.after_cancel(TIMER)
    title.config(text="timer", fg=RED)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS, CHECKS
    REPS += 1
    if REPS % 8 == 0:
        REPS = 0
        CHECKS = CHECKS + "✔️"
        title.config(text="Long break", fg=RED)
        check_marks.config(CHECKS)
        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        title.config(text="Short break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)  
    else:
        title.config(text="Stay focused")
        count_down(WORK_MIN * 60)
     

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global TIMER
    min_left = math.floor(count/60)
    sec_left = count % 60
    if sec_left < 10:
        sec_left = f"0{sec_left}"
    canvas.itemconfig(timer_text, text=f"{min_left}:{sec_left}")
    if count > 0:
        TIMER = window.after(900, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro(⏱)")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.config()
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(text=CHECKS, fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
window.mainloop()
