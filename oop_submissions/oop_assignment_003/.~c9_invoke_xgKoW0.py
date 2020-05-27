import math
class Car:
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

class RaceCar(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.nitro=0
    
    def start_engine(self):
        self._is_engine_started=True
    def accelerate(self):
        if self._is_engine_started==True:
            if self.nitro>0:
                self._current_speed=math.ceil(self.current_speed+self._acceleration+(self._acceleration*30//100))
                self.nitro-=10
            if self._current_speed<=self._max_speed:
                self._current_speed+=self._acceleration
            else:
                self._current_speed=self._max_speed
        else:
            self._cureent_speed=0
            print("Start the engine to accelerate")
    def apply_brakes(self):
        if self._current_speed>self._max_speed//2:
            self.nitro+=10
            
        if self._is_engine_started==True and self._current_speed>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._is_engine_started=False
            self._current_speed=0
    def sound_horn(self):
        if self._is_engine_started==True:
            print("Peep Peep")
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")        
        
        