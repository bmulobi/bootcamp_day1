


def data_type(arg):
    """function returns a message whose content depends on the data type 
       of the given input"""
       
    msg = ""
    
    # take care of string inputs
    if type(arg) is str:
        msg = len(arg)
    
    # take care of None inputs    
    if arg is None:
        msg = "no value"

     # take care of True inputs        
    if isinstance(arg,bool) and arg:
        msg = True 
    
    # take care of False inputs    
    if isinstance(arg,bool) and not arg:
        msg = False 
    
    # take care of integer inputs
    if type(arg) is int:
        
        if arg == 100:
            msg = "equal to 100"
                    
        if arg < 100:
            msg = "less than 100"
                
        if arg > 100:
            msg = "more than 100"        
    
    # take care of list inputs    
    if type(arg) is list:
           if len(arg) < 3:
               msg = None
           else: 
               msg = arg[2]               
             
    return msg 
    
#print data_type([1,2,3,4])    