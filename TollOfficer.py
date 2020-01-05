from tkinter import *
import os
import cx_Oracle
import ocr_text_extraction
import database_functions


def delete_screen6():
    screen6.destroy()


def print_bill():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Print Bill")
    screen7.geometry("150x100")
    Label(screen7, text="Connect with a printer. Bill will be printed")


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Successful Registration")
    screen3.geometry("1000x750")

    Label(screen3, text="Log In Success").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Scan Number Plate", width="20", height="2", command=dashboard).pack()


def wrong_password():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Wrong Password")
    screen4.geometry("1000x750")

    Label(screen4, text="Wrong Information", fg="red").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Try Again!", fg="red", width="20", height="2", command=login).pack()


def reg_user():
    brdg_info = brdg_id.get()
    tll_info = toll_id.get()
    bth_info = bth_id.get()

    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:
        curs = c.cursor()
        curs.callproc("BOOTH_MANAGER_REG", [brdg_info, tll_info, bth_info])
    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    brdg_id_entry.delete(0, END)
    toll_id_entry.delete(0, END)
    bth_id_entry.delete(0, END)

    Label(screen1, text="\n\n You have successfully completed your registration", fg="green",
          font=("Times New Roman", 13)).pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("1000x750")

    global brdg_id
    global toll_id
    global bth_id
    global brdg_id_entry
    global toll_id_entry
    global bth_id_entry

    brdg_id = StringVar()
    toll_id = StringVar()
    bth_id = StringVar()

    Label(screen1, text="Please enter your details").pack()
    Label(screen1, text="").pack()

    global username_entry
    global mail_entry
    global password_entry

    Label(screen1, text="Bridge ID").pack()
    brdg_id_entry = Entry(screen1, textvariable=brdg_id)
    brdg_id_entry.pack()

    Label(screen1, text="Toll Center ID ").pack()
    toll_id_entry = Entry(screen1, textvariable=toll_id)
    toll_id_entry.pack()

    Label(screen1, text="Booth_ID").pack()
    bth_id_entry = Entry(screen1, textvariable=bth_id)
    bth_id_entry.pack()

    Label(screen1, text="").pack()
    Button(screen1, text="Complete Registration", width="20", height="2", command=reg_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Log In")
    screen2.geometry("1000x750")

    Label(screen2, text="Please enter your details to login").pack()
    Label(screen2, text="").pack()

    global bridge_id_verify
    global bridge_id_entry1
    global tool_plaza_id_verify
    global tool_plaza_id_entry1
    global booth_id_verify
    global booth_id_entry1

    bridge_id_verify = StringVar()
    tool_plaza_id_verify = StringVar()
    booth_id_verify = StringVar()

    Label(screen2, text="Bridge ID").pack()
    bridge_id_entry1 = Entry(screen2, textvariable=bridge_id_verify)
    bridge_id_entry1.pack()

    Label(screen2, text="").pack()

    Label(screen2, text="Toll Plaza ID").pack()
    tool_plaza_id_entry1 = Entry(screen2, textvariable=tool_plaza_id_verify)
    tool_plaza_id_entry1.pack()

    Label(screen2, text="").pack()

    Label(screen2, text="Booth ID").pack()
    booth_id_entry1 = Entry(screen2, textvariable=booth_id_verify)
    booth_id_entry1.pack()

    Label(screen2, text="").pack()
    Button(screen2, text="Log In", width="30", height="2", command=login_verify).pack()


def login_verify():
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:
        curs = c.cursor()
        cnt = curs.callfunc("BOOTH_MANAGER_LOG_IN", cx_Oracle.NUMBER, [bridge_id_verify.get(), booth_id_verify.get(),
                                                                       tool_plaza_id_verify.get()])
        print(cnt)
        if cnt == 1.0:
            login_success()
        else:
            wrong_password()

    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)


def dashboard():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.geometry("1000x750")

    car_no = ocr_text_extraction.ocr_demo()
    owner = database_functions.get_car_owner(car_no)
    pre_balance = database_functions.get_balance(car_no)
    toll_amount = database_functions.get_toll_amount(car_no)
    updated_balance = pre_balance - toll_amount
    database_functions.update_balance(car_no, updated_balance)
    status = database_functions.car_pass(car_no)
    database_functions.event_log_update(car_no, bridge_id_verify.get(), booth_id_verify.get())

    Label(screen6, text="Welcome to TOLL TOOL").pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Car no : " + car_no).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Car Owner : " + owner).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Total Balance : " + str(pre_balance)).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Toll Amount : " + str(toll_amount)).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Remaining Balance : " + str(updated_balance)).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Car Status : " + status).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Print Bill", command=print_bill).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Log Out", command=delete_screen6).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("1000x750")
    screen.title("Toll Tool")
    Label(text="Toll Tool Officer", bg="grey", width="300", height="2", font=("Times New Roman", 13)).pack()
    Label(text="").pack()
    Button(text="Login", width="30", height="2", command=login).pack()
    ##Button(text="Login", width="30", height="2", command=screen.destroy).pack()
    Label(text="").pack()
    Button(text="Register", width="30", height="2", command=register).pack()

    screen.mainloop()


main_screen()
