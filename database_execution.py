import cx_Oracle


def execute_scripts_from_file(filename):
    fd = open(filename, 'r')
    sqlfile = fd.read()
    fd.close()

    sqlCommands = sqlfile.split(';')

    for command in sqlCommands:
        try:
            connection = cx_Oracle.connect('spl2/spl2@localhost/SYSTEM', encoding='UTF-8', nencoding='UTF-8')
            manager = connection.cursor()
            manager.execute(command)
            print('commands executed successfully')
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if manager:
                manager.close()
            if connection:
                connection.close()


execute_scripts_from_file("init.sql")
