import cx_Oracle
import os

def get_balance(a):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:

        curs = c.cursor()

        balance = curs.callfunc("GET_BALANCE", cx_Oracle.NUMBER, [a])
        print("BALANCE :", balance)
        curs.close()

    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    return balance


def get_car_owner(a):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')

    try:
        curs = c.cursor()
        owner_name = curs.callfunc("FIND_CAR_OWNER", cx_Oracle.NCHAR, [a])
        print("CAR OWNER: ",owner_name)
        curs.close()
    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    return owner_name


def get_toll_amount(a):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:

        curs = c.cursor()
        amount = curs.callfunc("GET_AMOUNT", cx_Oracle.NUMBER, [a])
        print("TOLL AMOUNT :", amount)
        curs.close()

    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    return amount

    ##new_balance = balance-amount
    ##print("Updated balance :", new_balance)


def update_balance(a,new_balance):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:

        curs = c.cursor()
        curs.callproc("UPDATE_BALANCE", [new_balance, a])
        curs.close()

    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)


def car_pass(a):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:

        curs = c.cursor()
        status = curs.callfunc("CAR_PASS", cx_Oracle.NCHAR, [a])
        curs.close()

    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    print("Car pass status :", status)
    return status


def event_log_update(a, bri_id, boo_id):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:
        curs = c.cursor()
        curs.callproc("EVENT_LOG", [a, bri_id, boo_id])
        curs.close()

    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    print("Event log updated"+ bri_id +" "+boo_id)


def user_login_verify(name, id):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:
        curs = c.cursor()
        num = curs.callfunc("USER_LOGIN", cx_Oracle.NUMBER, [name, id])
        curs.close()
    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    print("Login successful")
    return num


def user_acc_amount(id):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    try:
        curs = c.cursor()
        amount = curs.callfunc("USE_ACC_BALANCE", cx_Oracle.NUMBER, [id])
        curs.close()
    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)
    return amount


def user_history(id):
    c = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
    sid = str(id)
    s = "select * from EVENT where EVENT.N_ID="+sid
    print(s)
    try:
        curs = c.cursor()
        curs.execute(s)
        data = curs.fetchall()

        for row in data:
            print(row[3],row[4],row[5],row[6])
    except cx_Oracle.DatabaseError as ex:
        err, = ex.args
        print("Error code    = ", err.code)
        print("Error Message = ", err.message)
        os._exit(1)

    return data
