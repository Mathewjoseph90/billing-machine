def create_db():#function to create database when the program is run for the first time
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew")
    cur_obj = db_obj.cursor()
    q = "create database shop"
    try:
        cur_obj.execute(q)
    except Exception as e:
        print(e)
    finally:
        cur_obj.close()
        if db_obj.is_connected():
            db_obj.close()


def create_table_stock():# function to create table stock when the program is run for the first time
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    cur_obj = db_obj.cursor()
    q = "create table stock(iteam_num int primary key,iteam_name varchar(20) not null,price float not null)"
    try:
        cur_obj.execute(q)

    except Exception as e:
        db_obj.commit()
        print(e)
    finally:
        cur_obj.close()
        if db_obj.is_connected():
            db_obj.close()

def add_data_stock(iteam_num,iteam_name,price):# function to add more elements to the list of iteams in the store
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    cur_obj = db_obj.cursor()
    q = f"insert into stock values({iteam_num},'{iteam_name}',{price})"
    try:
        cur_obj.execute(q)
        db_obj.commit()
    except Exception as e:
        print(e)

    finally:
        cur_obj.close()
        if db_obj.is_connected():
            db_obj.close()


def create_table_billing():#function to create table bill when the program is run for the first time
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    cur_obj = db_obj.cursor()
    q = "create table bill(sn_no int primary key,name varchar(20) not null,quantity int not null,iteam_num int not null,foreign key(iteam_num) references stock(iteam_num))"
    try:
        cur_obj.execute(q)
    except Exception as e:
        print(e)
    finally:
        cur_obj.close()
        if db_obj.is_connected():
            db_obj.close()


def add_data_billing(sn_no,name,quantity,it_no):#fn to add data into the table bill
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    cur_obj = db_obj.cursor()
    print(it_no)
    try:
        q = "insert into bill values(%s,%s,%s,%s)"
        a = (sn_no,name,quantity,it_no)
        cur_obj.execute(q,a)
        db_obj.commit()
    except Exception as e:
        print(e)
    finally:
        cur_obj.close()
        if db_obj.is_connected():
            db_obj.close()        


def check_data_base():# fn to check whether databse is present in the system 
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew")
    cur_obj = db_obj.cursor()
    q = "show databases"
    cur_obj.execute(q)
    db_names = cur_obj.fetchall()
    if ('shop',) in db_names:
        return True
    else:
        return False


def check_table_bill():# fn to check whether table is present in the database
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew",database = 'shop')
    cur_obj = db_obj.cursor()
    cur_obj.execute("use shop")
    cur_obj.execute("show tables")
    tb_names = cur_obj.fetchall()
    if ('bill',)  in tb_names:
        return True
    else:
        return False 


def check_table_stock():# fn to check whether table is present in the database
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew",database = 'shop')
    cur_obj = db_obj.cursor()
    cur_obj.execute("use shop")
    cur_obj.execute("show tables")
    tb_names = cur_obj.fetchall()
    if ('stock',) in tb_names:
        return True
    else:
        return False 
