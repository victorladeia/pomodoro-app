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
reps = 0
CHECK_MARK = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 44))
    check_label.config(text="")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 44))
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 44))
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Focus", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 44))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min_count = count // 60
    sec_count = count % 60
    if min_count < 10:
        min_count = f"0{min_count}"
    if sec_count < 10:
        sec_count = f"0{sec_count}"

    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps // 2
        for work_session in range(work_sessions):
            mark += CHECK_MARK
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 44))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 138, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# START Button:
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# RESET Button:
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# --------------------------- MAIN LOOP
window.mainloop()
