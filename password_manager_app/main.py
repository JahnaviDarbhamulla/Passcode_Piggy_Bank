# -------------------------------libraries-----------------------------------#
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json

# import pyperclip

# ------------------------------------------------ UI SETUP --------------------------------------------#

window = Tk()
window.title("Passcode Piggy Bank")
canvas = Canvas(width="626", height="626", highlightthickness=0)
password_img = PhotoImage(file="password_page.png")
wallpaper = canvas.create_image(313, 313, image=password_img)

main_img = PhotoImage(file="main_page.png")
add_img = PhotoImage(file="add.png")
search_img = PhotoImage(file="search.png")


# -----------------------------------search_page-------------------------------------#
def go_to_search():
    def go_to_main_search():
        canvas.itemconfigure(wallpaper, state="hidden")
        canvas.create_image(313, 200, image=main_img)
        PPB_entry.place_forget()
        main_button.place_forget()
        enter.place_forget()
        add_btn.place(x=80, y=400)
        search_btn.place(x=350, y=400)
        website.place_forget()
        web_entry.place_forget()
        email.place_forget()
        email_entry.place_forget()
        home_page_button.place_forget()
        email_id_entry.delete(0, "end")

        web_site.place_forget()
        email_id.place_forget()
        website_entry.place_forget()
        email_id_entry.place_forget()
        search_button.place_forget()

    def search():
        web = website_entry.get()
        email_name = email_id_entry.get()

        try:
            with open("piggy_bank.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("piggy_bank.json", mode="w") as data_file:
                messagebox.showinfo(title=f"{web}", message=f"Mr. Pig: I am afraid there is no password saved"
                                                            f" for that website.")
                print("created a JSON file")

        else:

            if web in data:
                email = data[web]["email"]
                password = data[web]["password"]
                messagebox.showinfo(title=f"{web}",
                                    message=f"Mr. Pig: shhhh..Your details are \n\nEmail : {email} \n"
                                            f"Password : {password}  ")
            else:
                messagebox.showinfo(title=f"{web}", message=f"Mr. Pig: I am afraid there is no password saved"
                                                            f" for that website. oink!")

        finally:
            website_entry.delete(0, 'end')
            email_id_entry.delete(0, "end")
            email_id_entry.insert(END, "@email.com")

    canvas.itemconfigure(wallpaper, state="hidden")
    canvas.create_image(313, 313, image=search_img)
    add_btn.place_forget()
    search_btn.place_forget()

    web_site.place(x=80, y=400)
    email_id.place(x=80, y=440)

    website_entry.focus()
    email_id_entry.insert(0, "@email.com")

    website_entry.place(x=260, y=400)
    email_id_entry.place(x=260, y=440)

    search_button = Button(text="Search password from your piggy bank ", width=50, bg="#f9dfdc",
                           font=("Arial ", 11), command=search)
    search_button.place(x=100, y=550)
    home_page_button.place(x=500, y=10)
    home_page_button.config(command=go_to_main_search)
    home_page_button.config(bg="#b6c9f0")


# -----------------------------------main_page-----------------------------------#
def go_to_main():
    canvas.itemconfigure(wallpaper, state="hidden")
    canvas.create_image(313, 200, image=main_img)
    PPB_entry.place_forget()
    main_button.place_forget()
    enter.place_forget()
    add_btn.place(x=80, y=400)
    search_btn.place(x=350, y=400)



# -----------------------------------add_page-------------------------------------#
def go_to_add():
    def go_to_main_add():
        canvas.itemconfigure(wallpaper, state="hidden")
        canvas.create_image(313, 200, image=main_img)
        PPB_entry.place_forget()
        main_button.place_forget()
        enter.place_forget()
        add_btn.place(x=80, y=400)
        search_btn.place(x=350, y=400)
        website.place_forget()
        web_entry.place_forget()
        email.place_forget()
        email_entry.place_forget()
        password.place_forget()
        password_entry.place_forget()
        add_button.place_forget()
        pass_button.place_forget()
        home_page_button.place_forget()
        email_entry.delete(0, "end")


    # ---------------------------------------------- PASSWORD GENERATOR ------------------------------------#
    def generate_passcode():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = []

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        password_entry.insert(0, password)
        # pyperclip.copy(password)

    # ---------------------------------------------- SAVE PASSWORD ----------------------------------------#

    def save():
        web = web_entry.get()
        email_name = email_entry.get()
        passcode = password_entry.get()
        new_data = {
            web: {
                "email": email_name,
                "password": passcode
            }
        }
        if len(web) == 0 or len(passcode) == 0 or len(email_name) == 0:
            messagebox.showwarning(title="Opps, * snort snort *", message="Mr. Pig: Don't leave any feilds empty!")
        else:
            is_ok = messagebox.askokcancel(title="Confirm",
                                           message=f"These are the details entered \n\nEmail : "
                                                   f"{email_name}"
                                                   f" and \nPassword : {passcode}. \n\n"
                                                   f"Can Mr.Pig save it in the piggy bank ??")
            if is_ok:
                try:
                    with open("piggy_bank.json", mode="r") as pass_file:
                        data = json.load(pass_file)

                except FileNotFoundError:
                    with open("piggy_bank.json", mode="w") as pass_file:
                        print("created JSON file")
                        json.dump(new_data, pass_file, indent=4)
                else:

                    data.update(new_data)
                    with open("piggy_bank.json", mode="w") as pass_file:
                        json.dump(data, pass_file, indent=4)
                finally:
                    web_entry.delete(0, 'end')
                    email_entry.delete(0, "end")
                    email_entry.insert(END, "@email.com")
                    password_entry.delete(0, 'end')

    # ---------------------------------configurations for add_page----------------------#
    canvas.itemconfigure(wallpaper, state="hidden")
    canvas.create_image(313, 313, image=add_img)
    add_btn.place_forget()
    search_btn.place_forget()

    website.place(x=80, y=400)
    email.place(x=80, y=440)
    password.place(x=80, y=480)

    web_entry.focus()
    email_entry.insert(0, "@email.com")

    web_entry.place(x=260, y=400)
    email_entry.place(x=260, y=440)
    password_entry.place(x=260, y=480)

    pass_button = Button(text="Ask Mr.Pig for a password ! ", width=20, bg="#f9dfdc", command=generate_passcode)

    add_button = Button(text="Add password to your piggy bank ", width=50, bg="#f9dfdc", font=("Arial ", 11),
                        command=save)

    pass_button.place(x=430, y=480)

    add_button.place(x=100, y=540)

    home_page_button.place(x=500, y=10)
    home_page_button.config(command=go_to_main_add)
    home_page_button.config(bg="#caf7e3")


# -------------------------------reading the two files for username and password----------------------
with open("passcode.txt", mode="r") as file:
    name = file.readline()
with open("name_user.txt", mode="r") as file2:
    user = file2.readline()
canvas.create_text(300, 100,
                   text=f"                            Hello {user}  \n             Welcome to the Passcode Piggy Bank.  \n I'm Mr.Pig and I will help you save your passwords !",
                   fill="#536162", font=("Open Sans", 15, "bold"))


def check_pass():
    password_main = PPB_entry.get()

    if password_main == name:
        go_to_main()

    else:
        messagebox.showerror(title="Error", message="You have entered the wrong password !")


# ----------------------------------------------main_page_buttons---------------------------#

add_btn = Button(text="Add to piggy bank", width=30, height=3, bg="#f9dfdc", command=go_to_add)
search_btn = Button(text="Search from piggy bank", width=30, height=3, bg="#f9dfdc", command=go_to_search)
main_button = Button(width=28, bg="#f9dfdc", text=f"Let's check if you are {user}", command=check_pass)


# -------------------add page btns ------------------#

website = Label(text="Website : ", font=("Arial ", 13), bg="#fdc9cb")

email = Label(text="Email/Username : ", font=("Arial ", 13), bg="#fdc9cb")
password = Label(text="Password : ", font=("Arial ", 13), bg="#fdc9cb")

web_entry = Entry(width=40, bg="#f9f3f3", font=("Arial ", 11))
email_entry = Entry(width=40, bg="#f9f3f3", font=("Arial ", 11))
password_entry = Entry(width=20, bg="#f9f3f3", font=("Arial ", 11))


# ----------------search btns ------------------------#

web_site = Label(text="Website : ", font=("Arial ", 13), bg="#fdc9cb")
email_id = Label(text="Email/Username : ", font=("Arial ", 13), bg="#fdc9cb")

website_entry = Entry(width=40, bg="#f9f3f3", font=("Arial ", 11))

email_id_entry = Entry(width=40, bg="#f9f3f3", font=("Arial ", 11))

home_page_button = Button(text="Home Page", width=10,  font=("Arial ", 10))

enter = Label(text="Enter Password : ", font=("Arial ", 11), bg="#b0e0ec")
enter.place(x=130, y=530)
PPB_entry = Entry(width=25, bg="#f9f3f3", font=("Arial ", 11), show="*")
PPB_entry.place(x=270, y=530)
PPB_entry.focus()
canvas.pack()
main_button.place(x=210, y=570)

window.mainloop()
