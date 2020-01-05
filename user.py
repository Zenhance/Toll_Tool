from tkinter import *
import database_functions
import cx_Oracle


def lost_car():
    print("Car is lost")


def delete_screen3():
    screen3.destroy()


def delete_screen6():
    screen6.destroy()


def my_history():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("History")
    screen7.geometry("600x500")

    fs = "select * from EVENT where EVENT.N_ID="+str(password1)

    print(fs)

    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    curs = c.cursor()
    curs.execute(fs)
    history = curs.fetchall()

    Label(screen7, text="Passing time    Bridge      Number Plate        Booth").pack()
    for row in history:
        Label(screen7, text=(row[3], row[4], row[5], row[6])).pack()
        Label(screen7, text="").pack()


def my_balance():
    balance = database_functions.user_acc_amount(password1)
    print("Current balance: " + str(balance))

    Label(screen6, text="Current Balance"+str(balance)).pack()


def dashboard():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.geometry("600x500")

    Label(screen6, text="Welcome to TOLL TOOL").pack()
    Label(screen6, text="").pack()
    Button(screen6, text="My History", command=my_history).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="My Balance", command=my_balance).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Log Out", command=delete_screen6).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="").pack()
    Label(screen6, text="").pack()


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Successful Registration")
    screen3.geometry("600x500")

    Label(screen3, text="Log In Success").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Dashboard", command=dashboard).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Log Out", command=delete_screen3).pack()


def wrong_password():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Login Denied")
    screen4.geometry("600x500")

    Label(screen4, text="Wrong N_ID or Name", fg="red", font=("Times New Roman", 20)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Try Again", width="20", height="2", command=login).pack()


def reg_user():
    username_info = username.get()
    number_plate_info = number_plate.get()
    engine_info = engine.get()
    chassis_info = chassis.get()
    car_type_info = car_type.get()
    n_id_info = n_id.get()
    bank_account_info = bank_account.get()
    mobile_no_info = mobile_no.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(number_plate_info + "\n")
    file.write(engine_info + "\n")
    file.write(chassis_info + "\n")
    file.write(car_type_info + "\n")
    file.write(n_id_info + "\n")
    file.write(bank_account_info + "\n")
    file.write(mobile_no_info + "\n")
    file.write(password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    number_plate_entry.delete(0, END)
    engine_entry.delete(0, END)
    chassis_entry.delete(0, END)
    car_type_entry.delete(0, END)
    n_id_entry.delete(0, END)
    bank_account_entry.delete(0, END)
    mobile_no_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="\n\n You have successfully completed your registration", fg="green",
          font=("Times New Roman", 13)).pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("600x500")

    global username
    global number_plate
    global engine
    global chassis
    global car_type
    global n_id
    global bank_account
    global mobile_no
    global password

    global username_entry
    global number_plate_entry
    global engine_entry
    global chassis_entry
    global car_type_entry
    global n_id_entry
    global bank_account_entry
    global mobile_no_entry
    global password_entry

    username = StringVar()
    number_plate = StringVar()
    engine = StringVar()
    chassis = StringVar()
    car_type = StringVar()
    n_id = StringVar()
    bank_account = StringVar()
    mobile_no = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter your details").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()

    Label(screen1, text="Number Plate No").pack()
    number_plate_entry = Entry(screen1, textvariable=number_plate)
    number_plate_entry.pack()

    Label(screen1, text="Engine No").pack()
    engine_entry = Entry(screen1, textvariable=engine)
    engine_entry.pack()

    Label(screen1, text="Chassis No").pack()
    chassis_entry = Entry(screen1, textvariable=chassis)
    chassis_entry.pack()

    Label(screen1, text="Car Type").pack()
    car_type_entry = Entry(screen1, textvariable=car_type)
    car_type_entry.pack()

    Label(screen1, text="National ID No").pack()
    n_id_entry = Entry(screen1, textvariable=n_id)
    n_id_entry.pack()

    Label(screen1, text="Bank Account").pack()
    bank_account_entry = Entry(screen1, textvariable=bank_account)
    bank_account_entry.pack()

    Label(screen1, text="Mobile No").pack()
    mobile_no_entry = Entry(screen1, textvariable=mobile_no)
    mobile_no_entry.pack()

    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()

    Label(screen1, text="").pack()
    Button(screen1, text="Complete Registration", width="20", height="2", command=reg_user).pack()


def login_verify():
    global username1;
    username1 = username_verify.get()
    global password1;
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    if database_functions.user_login_verify(username1, password1) == 1:
        login_success()
    else:
        wrong_password()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Log In")
    screen2.geometry("600x500")

    Label(screen2, text="Please enter your details to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global username_entry1
    global password_entry1
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="N_ID.").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Log In", width="30", height="2", command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x500")
    screen.title("Toll Tool")
    Label(text="Toll Tool", bg="grey", width="300", height="2", font=("Times New Roman", 13)).pack()
    Label(text="").pack()
    Button(text="Login", width="30", height="2", command=login).pack()
    Label(text="").pack()
    Button(text="Register", width="30", height="2", command=register).pack()

    screen.mainloop()


main_screen()
