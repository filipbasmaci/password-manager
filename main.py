from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    entry_password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site_name = entry_website.get().title()
    email = entry_email.get()
    password = entry_password.get()
    data_string = f"{site_name} | {email} | {password}\n"
    new_data = {
        site_name:{
            "email":email,
            "password": password
        }
    }


    if len(site_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please fill all the entries.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            entry_website.delete(0,END)
            entry_email.delete(0,END)
            entry_password.delete(0,END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    input_site = entry_website.get().title()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found.", message="There is no data entered.")
    else:
        if input_site in data:
            messagebox.showinfo(title=f"{input_site} Info", message=f"Email: {data[input_site]["email"]}\nPassword: {data[input_site]["password"]}")
        else:
            messagebox.showinfo(title="Data not found.", message="There is no data existing.")






# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row= 0 , column= 1)

label_website = Label(text="Website:")
label_website.grid(row=1 , column=0)

entry_website = Entry(width=35,)
entry_website.grid(row= 1 , column= 1, sticky=E+W)
entry_website.focus()

button_search = Button(text="Search", command=find_password)
button_search.grid(row=1, column=2, sticky=E+W)

label_email = Label(text= "Email/Username:")
label_email.grid(row=2 , column=0)

entry_email = Entry(width=35)
entry_email.grid(row=2 , column=1, columnspan= 2, sticky=E+W)

label_password = Label(text="Password:")
label_password.grid(row= 3 , column= 0)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky=E+W)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky=E+W)






window.mainloop()
