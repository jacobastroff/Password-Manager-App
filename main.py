from tkinter import *
from tkinter import messagebox, Entry
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0,END)
    password_input.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_input.get()
    website = website_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email":email,
            "password":password
        }
    }
    if len(email) ==0 or len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title="Error", message="Error: Some fields have been left empty!")

    else:
        if messagebox.askokcancel(title="Confirm?", message=f'Here are your credentials: \nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}\n Is this OK?'):
            try:
                with open('passwords.json', mode="r") as password_file:
                    print("This has been executed")
                    data = json.load(password_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('passwords.json', mode="w") as _:
                    data = new_data
            except json.decoder.JSONDecodeError:
                with open('passwords.json', mode="w") as _:
                    data = new_data
            with open('passwords.json', mode="w") as password_file:
                json.dump(data, password_file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0,END)
            email_input.delete(0,END)
# ---------------------------- SEARCH WEBSITES ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open('passwords.json', mode='r') as passwords_file:
            data_dict = json.load(passwords_file)
            try:
                username = data_dict[website]['email']
                password = data_dict[website]['password']
                messagebox.showinfo(title=f"{website}",message=f"Username: {username}\nPassword:{password}")
            except KeyError:
                messagebox.showinfo(title="Error", message="No information is stored here for this website!")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No passwords or usernames saved for your account")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No passwords or usernames saved for your account")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config( padx = 50, pady = 50)
window.title("Password Manager")
canvas = Canvas(width=200, height = 200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column = 1, row = 1)
website_text = Label(text="Website:")
website_text.grid(row=2, column = 0)
email_text = Label(text="Email/Username: ")
email_text.grid(row=3, column = 0)
password_text = Label(text="Password: ")
password_text.grid(row=4, column=0)
website_input = Entry()
website_input.grid(column = 1, row=2, sticky='EW' )
website_input.focus()
email_input = Entry()
email_input.grid(column = 1, row = 3, columnspan = 2,sticky='EW' )
password_input: Entry = Entry()
password_input.grid(column=1 , row = 4,sticky='EW')
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row = 4, column = 2)
button_add_password = Button(text="Add", command=save_password)
button_add_password.grid(column=1, row=5, columnspan =2,sticky='EW' )
search_button = Button(text="Search",command=search)
search_button.grid(sticky="Ew", row=2,column=2)


mainloop()