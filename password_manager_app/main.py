# -------------------------------libraries-----------------------------------#
from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
# import pyperclip


# ------------------------------------------------ UI SETUP --------------------------------------------#

def go_to_main():
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

        password ="".join(password_list)
        password_entry.insert(0, password)
        # pyperclip.copy(password)



    # ---------------------------------------------- SAVE PASSWORD ----------------------------------------#

    def save():
        web = web_entry.get()
        email_name = email_entry.get()
        passcode = password_entry.get()
        if len(web) == 0 or len(passcode) == 0 or len(email_name) == 0:
            messagebox.showwarning(title="Opps, * snort snort *", message="Mr. Pig: Don't leave any feilds empty!")
        else:
            messagebox.askokcancel(title=website,
                                   message=f"These are the details of the details entered \nEmail : {email_name} and \nPassword : {passcode}. \nCan Mr.Pig save it in the piggy bank ??")

        with open("data.txt", mode="a") as pass_file:
            pass_file.write(f"Website: {web} \nemail_id: {email_name} \npassword: {passcode} \n\n")

        web_entry.delete(0, 'end')
        email_entry.delete(0, "end")
        email_entry.insert(END, "@email.com")
        password_entry.delete(0, 'end')

    canvas.itemconfigure(wallpaper, state="hidden")
    canvas.create_image(313, 200, image=main_img)
    PPB_entry.place_forget()
    main_button.place_forget()
    enter.place_forget()
    website = Label(text="Website : ", font=("Arial ", 13), bg="#fdc9cb")
    email = Label(text="Email/Username : ", font=("Arial ", 13), bg="#fdc9cb")
    password = Label(text="Password : ", font=("Arial ", 13), bg="#fdc9cb")
    website.place(x=80, y=400)
    email.place(x=80, y=440)
    password.place(x=80, y=480)

    web_entry = Entry(width=40, bg="#f9f3f3", font=("Arial ", 11))
    web_entry.focus()
    email_entry = Entry(width=40, bg="#f9f3f3", font=("Arial ", 11))
    email_entry.insert(END, "@email.com")
    password_entry = Entry(width=20, bg="#f9f3f3", font=("Arial ", 11))

    web_entry.place(x=260, y=400)
    email_entry.place(x=260, y=440)
    password_entry.place(x=260, y=480)

    pass_button = Button(text="Ask Mr.Pig for a password ! ", width=20, bg="#f9dfdc", command=generate_passcode)
    pass_button.place(x=430, y=480)

    add_button = Button(text="Add password to your piggy bank ", width=50, bg="#f9dfdc", font=("Arial ", 11),
                        command=save)
    add_button.place(x=100, y=550)


window = Tk()
canvas = Canvas(width="626", height="626", highlightthickness=0)
password_img = PhotoImage(file="password_page.png")
main_img = PhotoImage(file="main_page.png")
wallpaper = canvas.create_image(313, 313, image=password_img)

with open("personal.txt",mode="r") as file:
    name = file.readline()
with open("data.txt",mode="r") as file2:
    user = file2.readline()
canvas.create_text(300, 100, text=f"                            Hello {user}  \n             Welcome to the Passcode Piggy Bank.  \n I'm Mr.Pig and I will help you save your passwords !" , fill="#536162",font=("Open Sans", 15, "bold"))


def check_pass():
    password_main = PPB_entry.get()


    if password_main == name:
        go_to_main()

    else:
        messagebox.showerror(title="Error",message="You have entered the wrong password !")

main_button = Button(width=28, bg="#f9dfdc",text=f"Let's check if you are {user}",command = check_pass )
enter = Label(text="Enter Password : ", font=("Arial ", 11), bg="#b0e0ec")
enter.place(x=130, y=530)
PPB_entry = Entry(width=25, bg="#f9f3f3", font=("Arial ", 11),show="*")
PPB_entry.place(x=270, y=530)
PPB_entry.focus()
canvas.pack()
main_button.place(x=210, y=570)

window.mainloop()
