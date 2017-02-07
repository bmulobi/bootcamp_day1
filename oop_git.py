class Person:

    """Class person defines universal attributes of a person"""

    def __init__(self,name,date_of_birth,address,id_number,pin_number):
        
        """constructor initialises attributes for each instance"""
        
        # private members
        self.__id_number = id_number
        self.__pin_number = pin_number
         
        self._name = name
        self._date_of_birth = date_of_birth
        self._address = address
        
    # descriptive methods to modify instance attributes   
    def change_id_number(self,arg):
        self.__id_number = arg

    def change_pin_number(self,arg):
        self.__pin_number = arg
  
    def change_name(self,arg):
        self._name = arg

    def change_date_of_birth(self,arg):
        self._date_of_birth = arg

    def change_address(self,arg):
        self._address = arg

    # descriptive methods to access instance attributes    
    def get_id_number(self):
        return self.__id_number

    def get_pin_number(self):
        return self.__pin_number
  
    def get_name(self):
        return self._name

    def get_date_of_birth(self):
        return self._date_of_birth

    def change_address(self):
        return self._address  


class Employee(Person):
    
    """subclass of class person - defines the employee object"""
    def __init__(self,job,department,salary):
         
        self.__salary = salary 
         
        self._job = job
        self._department = department
    
    # descriptive methods to modify instance attributes    
    def change_job(self,arg):
        self._job = arg    
        
    def change_department(self,arg):
        self._department = arg

    def change_salary(self,arg):
        self.__salary = arg    
    
    # descriptive methods to access instance attributes    
    def get_job(self):
        return self._job

    def get_department(self):
        return self._department

    def get_salary(self):
        return self.__salary        
        
        
        