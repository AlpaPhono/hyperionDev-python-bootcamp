
import inventory
def main():
        while True:
        #presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.

            inventory.read_shoes_data()

            menu = input('''Select one of the following Options below:
        r - Register new shoe
        v - View stock
        a - Restock lowest shoe
        s - search for shoe via code
        c - On sale
        b - stock value
        e - Exit
        : ''').lower()

            if menu == 'r':
                inventory.capture_shoes()
               

            elif menu == 'v':
                inventory.view_all()


            elif menu == 'a':
                inventory.re_stock()

            elif menu == 's':
                
                print(inventory.search_shoe())

            elif menu == 'c':
                inventory.highest_qty()

            elif menu == 'b':
                inventory.value_per_item()
            
            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")
 


    





if __name__ == "__main__":
    main()