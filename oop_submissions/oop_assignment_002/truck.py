from oop_assignment_001.car import Car
class Truck(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        
        self._max_cargo_weight=max_cargo_weight
        self._cargo_weight=0
    @property
    def cargo_weight(self):
        return self._cargo_weight
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    def load(self,load):
        if load<0:
            raise ValueError('Invalid value for cargo_weight') 
        else:
            if self._current_speed==0:
                k=self._cargo_weight+load
                if k<=self._max_cargo_weight:
                    self._cargo_weight+=load
                else:
                    print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
            else:
                print("Cannot load cargo during motion")
    def unload(self,load):
        if load<0:
            raise ValueError('Invalid value for cargo_weight') 
        else:    
            if self._current_speed>0:
                print("Cannot unload cargo during motion")
            else:
                self._cargo_weight-=load
    def sound_horn(self):
        if self._is_engine_started==True:
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")                







'''class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self._color=color
       
        if max_speed<0:
            raise ValueError('Invalid value for max_speed') 
        self._max_speed=max_speed
        
        if acceleration<0:
            raise ValueError('Invalid value for acceleration')
        self._acceleration=acceleration
        
        if tyre_friction<0:
            raise ValueError('Invalid value for tyre_friction')
        self._tyre_friction=tyre_friction
        
        self._is_engine_started=False
        self._current_speed=0
    
    @property    
    def color(self):
        return self._color
   
    @property    
    def acceleration(self):
        return self._acceleration
    
    @property    
    def max_speed(self):
        return self._max_speed
    
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property    
    def current_speed(self):
        return self._current_speed
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    def start_engine(self):
        self._is_engine_started=True
    
    def accelerate(self):
        if self._is_engine_started==True:
            if self._current_speed<=self._max_speed:
                self._current_speed+=self._acceleration
            else:
                self._current_speed=self._max_speed
        else:
            self._cureent_speed=0
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
        if self._is_engine_started==True and self._current_speed>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._is_engine_started=False
            self._current_speed=0
            
    def sound_horn(self):
        if self._is_engine_started==True:
            print("Beap Beap")
        else:
            print("Start the engine to sound_horn")
    
    def stop_engine(self):
        self._is_engine_started=False
class Truck(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        
        self._max_cargo_weight=max_cargo_weight
        self._cargo_weight=0
    @property
    def cargo_weight(self):
        return self._cargo_weight
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    def load(self,load):
        if load<0:
            raise ValueError('Invalid value for cargo_weight') 
        else:
            if self._current_speed==0:
                k=self._cargo_weight+load
                if k<=self._max_cargo_weight:
                    self._cargo_weight+=load
                else:
                    print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
            else:
                print("Cannot load cargo during motion")
    def unload(self,load):
        if load<0:
            raise ValueError('Invalid value for cargo_weight') 
        else:    
            if self._current_speed>0:
                print("Cannot unload cargo during motion")
            else:
                self._cargo_weight-=load
    def sound_horn(self):
        if self._is_engine_started==True:
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")'''                
    
        
            
            
        
            
        
        
        
        