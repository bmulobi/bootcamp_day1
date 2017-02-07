class Car(object):
    """class provides template to instantiate different types of vehicles"""

    # setting some default values
    def __init__(self, name='General', model='GM', vtype=None):
        self.name = name
        self.model = model
        self.vtype = vtype
        self.speed = 0
        self.moving_speed = 0

        # setting num_of _doors depending on car name
        if self.name == 'Koenigsegg' or self.name == 'Porshe':
           self.num_of_doors = 2
        else:
           self.num_of_doors = 4
        
        # setting num_of _wheels depending on vehicle type
        if self.vtype == 'trailer':
           self.num_of_wheels = 8
        else:
           self.num_of_wheels = 4
 
    def is_saloon(self):
        """if the vehicle type is not trailer
         then function sets it to saloon"""
      
        if self.vtype is not 'trailer':
            self.vtype == 'saloon'
            return True
        return False

    def drive(self, moving_speed):
        """sets moving speed of vehicle based on argument passed"""
      
        if self.moving_speed == 3 or self.name == 'Mercedes' or self.vtype =='saloon':
           self.speed = 1000
           
        if self.moving_speed == 7 or self.name == 'MAN' or self.vtype == 'trailer':
           self.speed = 77
         

        return self
        
   