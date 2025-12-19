import tkinter as tk
from datetime import datetime

def update_countdown():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1, 0, 0, 0)

    if now > new_year:
        new_year = datetime(now.year, 1, 1, 0, 0, 0)

    time_left = new_year - now

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    label_days.config(text=f"{days:02d}")
    label_hours.config(text=f"{hours:02d}")
    label_minutes.config(text=f"{minutes:02d}")
    label_seconds.config(text=f"{seconds:02d}")
    root.after(1000, update_countdown)

root = tk.Tk()
root.title("🎄 До Нового Года осталось:")
root.configure(bg='#0a2e36')

font_large = ("Courier", 48, "bold")
font_small = ("Arial", 14)

frame = tk.Frame(root, bg='#0a2e36')
frame.pack(expand=True)

tk.Label(frame, text="ДНЕЙ", font=font_small, bg='#0a2e36', fg='white').grid(row=0, column=0, padx=10)
tk.Label(frame, text="ЧАСОВ", font=font_small, bg='#0a2e36', fg='white').grid(row=0, column=1, padx=10)
tk.Label(frame, text="МИНУТ", font=font_small, bg='#0a2e36', fg='white').grid(row=0, column=2, padx=10)
tk.Label(frame, text="СЕКУНД", font=font_small, bg='#0a2e36', fg='white').grid(row=0, column=3, padx=10)

label_days = tk.Label(frame, text="00", font=font_large, bg='#1a4a5a', fg='#4afc9f', width=3)
label_hours = tk.Label(frame, text="00", font=font_large, bg='#1a4a5a', fg='#4afc9f', width=3)
label_minutes = tk.Label(frame, text="00", font=font_large, bg='#1a4a5a', fg='#4afc9f', width=3)
label_seconds = tk.Label(frame, text="00", font=font_large, bg='#1a4a5a', fg='#4afc9f', width=3)

label_days.grid(row=1, column=0, padx=10, pady=10)
label_hours.grid(row=1, column=1, padx=10, pady=10)
label_minutes.grid(row=1, column=2, padx=10, pady=10)
label_seconds.grid(row=1, column=3, padx=10, pady=10)

update_countdown()
root.mainloop()
