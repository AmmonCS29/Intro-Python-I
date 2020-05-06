# # Python program to check if  
# # given number is prime or not 
  
# num = 12
  
# # If given number is greater than 1 
# if num > 1: 
      
#    # Iterate from 2 to n / 2  
#    for i in range(2, num//2): 
         
#        # If num is divisible by any number between  
#        # 2 and n / 2, it is not prime  
#        if (num % i) == 0: 
#            print(num, "is not a prime number") 
#            break
#    else: 
#        print(num, "is a prime number") 
  
# else: 
#    print(num, "is not a prime number") 

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))