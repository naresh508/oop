class Deer:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        self._age_in_months=age_in_months
        if self._age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(self._age_in_months))
        
        self._breed=breed
        
        self._required_food_in_kgs=required_food_in_kgs
        if self._required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
    @property
    def age_in_months(self):
        return self._age_in_months
    @property    
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self._required_food_in_kgs+=2
        self._age_in_months+=1

    def make_sound(self):
        print("Buck Buck")
    
    def breathe(self):
        print("Breathe in air")


class Lion(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
    
    def grow(self):
        self._required_food_in_kgs+=4
        self._age_in_months+=1

    def make_sound(self):
        print("Roar Roar")
    
    def breathe(self):
        print("Breathe in air")
        
    def hunt(self):
        pass    

class Shark(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
    
    def grow(self):
        self._required_food_in_kgs+=8
        self._age_in_months+=1

    def make_sound(self):
        print("Shark Sound")
    
    def breathe(self):
        print("Breathe oxygen from water")
        
    def hunt(self):
        pass    

class GoldFish(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
    
    def grow(self):
        self._required_food_in_kgs+=0.2
        self._age_in_months+=1

    def make_sound(self):
        print("Hum Hum")
    
    def breathe(self):
        print("Breathe oxygen from water")            

class Snake(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
    
    def grow(self):
        self._required_food_in_kgs+=0.5
        self._age_in_months+=1

    def make_sound(self):
        print("Hiss Hiss")
    
    def breathe(self):
        print("Breathe in air")
        
    def hunt(self):
        pass    
        
class Zoo:
    count=[]
    def __init__(self):
        self._list_animals=[]
        self._reserved_food_in_kgs=0
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    
    def add_food_to_reserve(self,value):
        self.reserved_food_in_kgs+=value
        return self.reserved_food_in_kgs
        
    def add_animals(self,animal):
        self._list_animals.append(animal)
        self.count.append(animal)
        
    def count_animals(self):
        return len(self._list_animals)
        
    def feed(self,animal):
        if self.reserved_food_in_kgs>0:
            self.reserved_food_in_kgs-=self.required_food_in_kgs
            return animal.grow()
    
    @classmethod
    def count_animals_all_zoos(cls,animal):
        return cls.count
        
#pass
    
    @staticmethod
    def count_animals_in_given_zoos(zoo):
        
        pass

deer=Deer(1,"Elk",10)
lion=Lion(1,"Elk",10)
shark=Shark(1,"Elk",10)
goldfish=GoldFish(1,"Elk",10)
snake=Snake(1,"Elk",10)


        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
            
            
        