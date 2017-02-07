def fizz_buzz(num):

    """function returns a message whose content depends on whether
       the given input is divisible by 3 or 5 or both or none"""
       
    msg = ''
    
    # if divisible by 3
    if num % 3 == 0 and num % 5 != 0:
        msg = 'Fizz'
    
    # if divisible by 5    
    elif num % 5 == 0 and num % 3 != 0:
        msg = 'Buzz'    
    
    # if divisible by 3 and 5   
    elif num % 5 == 0 and num % 3 == 0:
        msg = 'FizzBuzz'    
    
    # if not divisible by 3 and 5     
    else: 
        msg = num 

    return msg    