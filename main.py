from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)
    # print(f"Your password is: {password}")


# for char in password_list:
#     password += char

# password_list = []
#
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#     password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#     password_list += random.choice(numbers)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    passwords = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": passwords
        }}

    if len(website) == 0 or len(passwords) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty!")
    else:
        # messagebox.showinfo(title="Title", message="Message")
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details enter: \nEmail: {email} "
        #                                               f"\nPassword: {passwords} \nDo you want to save it?")
        # if is_ok:
        # with open("data.txt", "a") as data_file:
        #     data_file.write(f"{website} | {email} | {passwords}\n")
        #     website_entry.delete(0, END)
        #     password_entry.delete(0, END)
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website} | {email} | {passwords}\n")
                # json.dump(new_data, data_file, indent=4)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # print(data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Invalid Request", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Search Error", message=f"{website} not found, "
                                                              f"Kindly check your spelling and search again")

# ---------------------------- UI SETUP ------------------------------- #


app = Tk()
app.title("Password Manager")
logo_img = PhotoImage(file="logo.png")

# app.iconbitmap(r"logo2.ico")
app.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "hacktech224@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# Button
search_button = Button(text="search", width=12, command=find_password)
search_button.grid(row=1, column=2)
generate_password = Button(text="Generate Pass", command=generate_passwords)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)

app.mainloop()
