import tkinter as tk

BG = '#EBA64E'
window = tk.Tk()
window.title("Disappearing Text App")
window.config(bg=BG, padx=20, pady=10)
window.minsize(400, 375)
counter = 0
direction = tk.Label(text="5 seconds after you stop typing, your message will disappear!")
direction.grid(row=4, column=1, padx=20)
text = ""
textbox = tk.Text(height=20, width=60)
textbox.focus()
textbox.grid(row=3, column=1, padx=10, pady=10)

title = tk.Label(window, text="Write a top secret message.")
title.grid(row=0, column=1)


def text_disappear():
    textbox.delete(1.0, 'end')
    textbox.insert('end', "")

def reset():
    global counter, text
    if text == textbox.get(1.0, 'end'):
        if counter == 5:
            window.after(500, text_disappear)
            counter = -1
        window.after(500, reset)
        counter += 1
    else:
        window.after(500, reset)
        text = textbox.get(1.0, 'end')
        counter = 0

window.after(500, reset)
window.mainloop()
