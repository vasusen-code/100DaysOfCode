from tkinter import *
from tkinter import messagebox
from random import choice, randint

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

capital_letters = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M".split(" ")
small_letters = [letter.lower() for letter in capital_letters]
symbols = "! @ # $ % ^ & * - + = ".split(" ")

def random_pasword():
    password =  choice(capital_letters) 
    password = password + choice(symbols)
    for i in range(4):
        password = password + choice(small_letters)
    password = password + choice(symbols)
    for i in range(4):
        password = password + f"{randint(0, 9)}"
    return password
    
def generate_password():
    password = random_pasword()
    password_entry.insert(0, password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    id = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(id) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Make sure you have filled all of the values.")
        return 
    
    is_ok = messagebox.askokcancel(title="website", message=f"These are the details, {website} | {id} | {password}\n Do you want to save it?")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {id} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

website_label = Label(text="Website")
website_label.grid(row=0, column=0)
website_entry = Entry(width=41)
website_entry.grid(row=0, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="E-mail/Username")
email_label.grid(row=1, column=0)
email_entry = Entry(width=41)
email_entry.grid(row=1, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=2, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=2, column=1)
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=2, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=3, column=1, columnspan=2)
window.mainloop()
