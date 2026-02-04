if __name__ == '__main__':
    n = int(input().strip())
    if n%2==0 and (n in range(2,5) or n>20):
        print("Not Weird")
    elif (n%2==0 and n in range(6,20)):
        print("Weird")
    else:
        print("Weird")
       
    
    
