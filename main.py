
from time import ctime


def get_number_input(prompt):
    ''' 
    use prompt to collects input and return float
    '''
    value = None
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value

        except KeyboardInterrupt:
            exit()
        
        except ValueError as e:
            print("Invalid input")
            print(e, file=ERROR_FILE)
            pass

def main():
    while True:
        client_name = input("What is the customer\'s name?: ")
        
        if not client_name:
            break


        while True:
            product_name = input("What is the product name?: ")
            if not product_name:
                break

            product_qty = get_number_input(f"How many {product_name} was purchased?: ")
            product_price = get_number_input(f"How much is {product_name}?: ")



if __name__ == '__main__':
    # superglobals
    ERROR_FILE = open('error_log.txt', 'a')
    
    #the 
    main()

    #close
    ERROR_FILE.close()


