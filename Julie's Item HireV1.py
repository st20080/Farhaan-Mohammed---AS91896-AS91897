#Julie's Party Hire Store Tracker

from tkinter import*

count = 0
return_count = 1

#Quit the Program
def quit(): 
    main_window.destroy()

#Store the Data
def store_details ():
    global print_details, name, receipt, item, quantity, list_entries, total_names, name_display, receipt_display, item_display,  quantity_display, count

    #Setting Values to x
    name_display = "x"
    receipt_display = "x"
    item_display = "x"
    quantity_display = "x"
    
    #Checking if the Name value is a number
    enter_name = Label(main_window, font=("Bold"), text="")
    enter_name.grid(row=1, column=4)
    if name.get().isnumeric():
        enter_name.config(text="Please Enter a Name")
    else:
        enter_name.config(text="                                        ")
        name_display = name.get()
        
        
    #Checking if the receipt value is a number
    enter_receipt_number = Label(main_window, font=("Bold"), text="")
    enter_receipt_number.grid(row=2, column=4)
    try:
        int(receipt.get())
        enter_receipt_number.config(text="                                        ")
        receipt_display = receipt.get()
    except ValueError:
        enter_receipt_number.config(text="Please Enter a Number")

    
        #Checking if the Item value is a number
    enter_item = Label(main_window, font=("Bold"), text="")
    enter_item.grid(row=3, column=4)
    if item.get().isnumeric():
        enter_item.config(text="Please Enter a Name")
    else:
        enter_item.config(text="                                        ")
        item_display = item.get()
        
        
    #Checking if the quantity value is an integer
    enter_quantity_number = Label(main_window, font=("Bold"), text="")
    enter_quantity_number.grid(row=4, column=4)
    try:
        int(quantity.get())
        enter_quantity_number.config(text="                                        ")
        quantity_display = quantity.get()
    except ValueError:
        enter_quantity_number.config(text="Please Enter a Number")




#Print the Data
def print_details ():
    global print_details, name, receipt, item, quantity, list_entries, total_names, name_display, receipt_display, item_display,  quantity_display, count

    #If the Values are entered correctly proceed with code
    if name_display != "x" and receipt_display != "x" and item_display != "x" and quantity_display != "x":
        
        #Increase number of records
        if count < 500: count += 1
    
        #Makes Labels for Row, Name, Receipt No., Item and Quantity
        Label(main_window,text="Row").grid(column=0,row=10, pady=(20,5))
        Label(main_window,text="Name").grid(column=1,row=10, pady=(20,5))
        Label(main_window,text="Receipt No.").grid(column=2,row=10, pady=(20,5))
        Label(main_window,text="Item").grid(column=3,row=10, pady=(20,5))
        Label(main_window,text="Quantity").grid(column=4,row=10, padx=(35,0), pady=(20,5))

        #Displays the Label values
        Label(main_window, text=count).grid(column=0,row=count+11)
        Label(main_window, text=(name_display)).grid(column=1,row=count+11)
        Label(main_window, text=(receipt_display)).grid(column=2,row=count+11)
        Label(main_window, text=(item_display)).grid(column=3,row=count+11)
        Label(main_window, text=(quantity_display)).grid(column=4,row=count+11)
        main_window.geometry("")

        #Sets teh Values back to x
        name_display = "x"
        receipt_display = "x"
        item_display = "x"
        quantity_display = "x"

#Returning an item   
def return_item():
    global return_count,count
    if return_count <= count:
        Label(main_window, text="             ").grid(column=0,row=return_count+11)
        Label(main_window, text="                                    ").grid(column=1,row=return_count+11)
        Label(main_window, text="                   ").grid(column=2,row=return_count+11)
        Label(main_window, text="                                    ").grid(column=3,row=return_count+11)
        Label(main_window, text="                   ").grid(column=4,row=return_count+11)
        return_count += 1
        
#The Interface of the Program
def GUI(): 
    global details, name, receipt, item, quantity, list_entries, total_names, return_item_label
    
    #Name
    Label(main_window, text="Name :") .grid(row=1, column=1, padx=20) #Making a Label for the Name Entry
    name = Entry(main_window)
    name.grid(row=1, column=2, padx=10, pady=10, columnspan=2)


    #Reciept
    Label(main_window, text="Reciept No. :") .grid(row=2, column=1) #Making a Label for the Reciept Number
    receipt = Entry(main_window)
    receipt.grid(row=2, column=2, padx=10, pady=10, columnspan=2)

    #What item was Hired
    Label(main_window, text="Item :") .grid(row=3, column=1) #Making a Label for the Item that was Hired
    item = Entry(main_window)
    item.grid(row=3, column=2, padx=10, pady=10, columnspan=2)

    #Quantity
    Label(main_window, text="Quantity :") .grid(row=4, column=1) #Making a Label for the Quantity of Items Hired
    quantity = Entry(main_window)
    quantity.grid(row=4, column=2, padx=10, pady=10, columnspan=2)

    #Quit Button
    Button(main_window, text="Quit", width= 8, command= quit) .grid(row=0, column=1, padx=5, pady = 10) #Making a button to Quit the Program

    #Store Details
    Button(main_window, text="Store Details", width= 8, command= store_details) .grid(row=0, column=2, padx=5, pady = 10) #Making a Button to Store the details you enter

    #Print Details
    Button(main_window, text="Print Details", width= 8, command= print_details) .grid(row=0, column=3, padx=5, pady = 10) #Button to execute the print command

    #Return Item Button
    Button(main_window, text="Return Item", width= 8, command= return_item) .grid(row=0, column=4, padx=5, pady = 10) #Button to execute the return item command

#Running the Interface
def main():
    global main_window
    global details, name, receipt, item, quantity, list_entries, total_names
    main_window =Tk()
    GUI()
    
 
    main_window.title("Julie's Tracker")
    
    main_window.mainloop()

main()
