def display_bill():#Fn to display the final bill
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    cur_obj = db_obj.cursor()
    try:
    
        q = "select iteam_name as NAME,sum(quantity) as QUANTITY,sum(quantity)*price as PRICE from stock,bill where stock.iteam_num = bill.iteam_num group by iteam_name"
        cur_obj.execute(q)
        name_iteam = cur_obj.fetchall()
        total = 0
        print("NAME","\tQUANTITY","PRICE")
        for i in name_iteam:
            print(i[0],'\t',i[1],'\t',i[2])
            total = total +i[2]
        print("Total = ",total)
    except Exception as e:
        print(e)



def to_get_iteam_number(name):#fn to get iteam name
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    try:
        cur_obj = db_obj.cursor()
        cur_obj.execute(f"select * from stock where iteam_name = '{name}'")
        num_obj = cur_obj.fetchall()
        return num_obj[0][0]
    except Exception as e:
        print(e)




def display_iteamlist():#fn is display the list of iteams present in the store
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    cur_obj = db_obj.cursor()
    cur_obj.execute("use shop")
    q = "select * from stock"
    try:
        cur_obj.execute(q)
        list_obj = cur_obj.fetchall()
        for i in list_obj:
            print(i)
    except Exception as e:
        print(e)

def delete_table_bill():#fn to delete the table bill after the printing the final bill
    import mysql.connector
    db_obj = mysql.connector.connect(host = "localhost", user = "root", password = "Mathew", database = 'shop')
    cur_obj = db_obj.cursor()
    try:
        cur_obj.execute("drop table bill")
        db_obj.commit()
    except Exception as e:
        print(e)