from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global checks
    global reps
    reps = 0
    checks = ""
    title.config(text="Timer", fg=GREEN)
    check.config(text=checks)
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = 60*WORK_MIN
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps%2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global checks
        start_timer()
        if reps%2 == 0:
            checks += "✔"
            check.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=30, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# title
title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), foreground=GREEN, background=YELLOW)
title.grid(column=1, row=0)

# Buttons

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

# checks
check = Label( font=("Arial", 15), foreground=GREEN, background=YELLOW)
check.grid(column=1, row=3)

window.mainloop()
