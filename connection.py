import cx_Oracle


def table_creation():
    citizen_table_query = "CREATE TABLE CITIZEN(\
                            N_ID NUMBER,\
                            DRIVING_LICENSE_NO VARCHAR2(25),\
                            MOBILE_NO NUMBER,\
                            CHECK (LENGTH(MOBILE_NO)=11),\
                            PRIMARY KEY(DRIVING_LICENSE_NO)\
                            )"


    try:
        connection = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM')
        manager = connection.cursor()
        manager.execute(citizen_table_query)
        print("Table Created successful")

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)

    finally:
        if manager:
            manager.close()
        if connection:
            connection.close()


def table_delete(table_name):

    table_delete_query = "DROP TABLE " + table_name

    try:
        connection = cx_Oracle.connect('spl2/spl2@localhost')
        manager = connection.cursor()
        manager.execute(table_delete_query)
        print("table deleted successfully")

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle",e)

    finally:
        if manager:
            manager.close()
        if connection:
            connection.close()
