def gether_data():
    n1 = input("Primeiro valor: ")
    n2 = input("Segundo valor : ")
    op = input("operação: ") 
    return n1, n2, op

def main():
    n1, n2, op = gether_data()
    
    print(eval(n1+op+n2))
    
    return None 

if __name__ == "__main__":
    main()

def get_operation():
    op = input("Operação: ")
    return op