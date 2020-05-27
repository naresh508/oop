class Animal:
    sound=""
    breath=""
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        
        
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        
        self._breed=breed
        
        
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        
    @property    
    def age_in_months(self):
        return self._age_in_months
        
    @property    
    def breed(self):
        return self._breed
        
    @property    
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    @classmethod
    def breathe(cls):
        print(cls.breath)


class Deer(Animal):
    
    def grow(self):
        self._required_food_in_kgs+=2
        self._age_in_months+=1
    
    sound="Buck Buck"
    
    breath="Breathe in air"
    
    
    

    

class Lion(Animal):
    sound="Roar Roar"
    
    breath="Breathe in air"
    def grow(self):
        self._required_food_in_kgs+=4
        self._age_in_months+=1
        
    

    def hunt(self,a):
        if "Deer" in a.animal_list:
            a.animal_list.remove("Deer")
        else:    
            print("no deers to hunt")  

class Shark(Animal):
    sound="Shark Sound"
        
    breath="Breathe oxygen from water"
   
    
    def grow(self):
        self._required_food_in_kgs+=8
        self._age_in_months+=1
    
    
    
    def hunt(self,a):
        if "GoldFish" in a.animal_list:
            a.animal_list.remove("GoldFish")
        else:    
            print("no GoldFish to hunt")
          

class GoldFish(Animal):
    sound="Hum Hum"
    
    breath="Breathe oxygen from water"    
    
    def grow(self):
        self._required_food_in_kgs+=0.2
        self._age_in_months+=1

    

class Snake(Animal):
    sound="Hiss Hiss"
    
    breath="Breathe in air"
    
    def grow(self):
        self._required_food_in_kgs+=0.5
        self._age_in_months+=1
    
    def hunt(self,a):
        if "Deer" in a.animal_list:
            a.animal_list.remove("Deer")
        else:    
            print("no deers to hunt")  
            
class Zoo:
    
    total_count  =[]
    
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.animal_list = []
        
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_animals(self,animal):
        self.animal_list.append(animal)
        self.total_count.append(animal)
        
        
    def count_animals(self):
        return len(self.animal_list)
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
        
    def feed(self,animal):
        food = animal._required_food_in_kgs
        if self._reserved_food_in_kgs >0:
            animal.grow()
            self._reserved_food_in_kgs -=food
            
            
    @classmethod        
    def count_animals_in_all_zoos(cls):
        return len(cls.total_count)
        
    @staticmethod    
    def count_animals_in_given_zoos(self,zoo):
        c = 0
        for i in zoo:
            c+=i.count_animals()
        return c            

    
    
    
        
           
"""
'''class Animal:
    sound = "sound"
    breath = "air"
    increase_required_food_in_kgs = 1
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        
        
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        
        self._breed=breed
        
        
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        
    @property    
    def age_in_months(self):
        return self._age_in_months
        
    @property    
    def breed(self):
        return self._breed
        
    @property    
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    @classmethod
    def breathe(cls):
        print(cls.breath)

    def grow(self):'''"""
        
        















        
        
    










    
"""
'''deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
deer.age_in_months
deer.breed
print(deer.required_food_in_kgs)
deer.grow()
deer.required_food_in_kgs
z=Zoo()
z.add_animals(deer)
z.add_food_to_reserve(1000)
print(z.reserved_food_in_kgs)
z.feed(deer)
print(z.reserved_food_in_kgs)'''
zoo=Zoo()
d=Deer(1,'elk',10)
l=Lion(1,'elk',10)
s=Shark(1,'elk',10)
gf=GoldFish(1,'elk',10)
sn=Snake(1,'elk',10)
zoo.add_animals(d)
Zoo.count_animals_in_given_zoos([zoo])
"""
        