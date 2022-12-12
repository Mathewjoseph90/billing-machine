print(("\t"*6) +"BILLING MACHINE")

ch = 1
while ch ==1:

    print("1.ADD MORE ITEAMS TO LIST OF ITEAMS PRESENT IN THE STORE")
    print("2.ADD ITEAM TO THE BILL")
    print("3.DISPLAY THE LIST OF ITEAMS AT THE STOCK")
    print("4.ISSUE THE BILL")
    print("5.EXIT")
    dis = int(input("choice:"))
    import addition as ad
    import billing as bl
    if dis == 1:
        if ad.check_data_base() == False:
            ad.create_db("shop")
            print("Created database please choose again")
        else:
            iteam_num = int(input("Enter the iteam number:"))
            iteam_name = input("Enter the iteam name:")
            price = float(input("Enter the price of the iteam:"))
            if ad.check_table_stock() == False:
                ad.create_table()
                ad.add_data_stock(iteam_num,iteam_name,price)
            else:
                ad.add_data_stock(iteam_num,iteam_name,price)
    elif dis == 2:
            sn_no = int(input("Enter the serial number:"))
            quantity = int(input("Enter the quantity of iteam:"))
            name_iteam = input("Enter the name of the iteam:")
            if ad.check_data_base() == False:
                ad.create_db("shop")
            if ad.check_table_bill() == False:
                ad.create_table_billing()
                it_no = bl.to_get_iteam_number(name_iteam)
                ad.add_data_billing(sn_no,name_iteam,quantity,it_no)
            else:
                it_no = bl.to_get_iteam_number(name_iteam)
                ad.add_data_billing(sn_no,name_iteam,quantity,it_no)

    elif dis == 3:
        if ad.check_data_base() == False:
            ad.create_db()
            ad.create_table_billing()
            bl.display_iteamlist()
        else:
            bl.display_iteamlist()

    elif dis == 4:
        if ad.check_data_base() == False:
            ad.create_db()
            ad.create_table_billing()
            bl.display_bill()
        else:
            bl.display_bill()
    elif dis == 5:
        if ad.check_table_bill() == True:
            bl.delete_table_bill()
        break
    else:
        print("Enter a valid number")