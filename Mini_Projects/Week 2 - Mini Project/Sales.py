############################     MINI PROJECT 2 (Week 2)      ###############################

################################   Smart Sales Analytics System   ##################################
#######################   Used Python : Loops , List, Conditions ############################


products =[]
sales=[]

while True:
    print("\n===== Smart Sales Analytics System ====")
    print("1.Add Sales Records")
    print("2.View Sales Records")
    print("3.Sales Analytics")
    print("4.Search Product")
    print("5.Exit")

    choice = input("Enter Your Choice :")

    ## 1 Add Sales Record 

    if choice =="1":

        product_name =input("Enter The Product Name :")
        sales_amount = float(input("Enter The Amount :"))

        products.append(product_name)
        sales.append(sales_amount)

        print("Sales Record Added Successfully!")

    ## 2 View Sales Record 

    elif choice =="2":

        if len(products) ==0:
            print("No Sales Record Available !!!")

        else:
            print("\n ------- Sales Record -------")

            for i in range(len(products)):
                print("Product :",products[i],"| Sales :", sales[i])

    
    ## 3 Sales anaytics 

    elif choice =="3":

        if len(sales) ==0:
            print("No Sales Data Available.")

        else:
            total_sales = sum(sales)

            average_sales = total_sales / len(sales)

            highest_sale = max(sales)

            lowest_sale = min(sales)

            highest_index = sales.index(highest_sale)

            lowest_index = sales.index(lowest_sale)

            print("\n ------- Sales Analytics ------")
            print("Total Sales :", total_sales)
            print("Average Sales :", average_sales)
            print("Highest Sales :", products[highest_index],"-" ,highest_sale)
            print("Lowest Sales :", products[lowest_index],"-" ,lowest_sale)


            print("\n ------- Performance Category -------")

            for i in range(len(sales)):

                if sales[i] >5000:
                    category ="High Performance"
                elif sales[i] >= 2000:
                    category = "Medium Performance"
                else:
                    category = "Low Performance"

                print(products[i], "-", sales[i], ":", category)

    

    ## 4 Search Product 

    elif choice =="4":

        search_product = input("Enter Product Name To Search :")

        if search_product in products:

            index = products.index(search_product)
            print("Product Found:", search_product)
            print("Sales Amount: ", sales[index])

        else:
            print("Product Not Found !!!")

    
    ## 5 Exit 

    elif choice=="5":
        print("Exit The System... Thank You!")
        break
    else:
        print("Invalid Choice! Please try again.")
