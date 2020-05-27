class Pokemen:
    soun_d=""
    ru_n=""
    swi_m=""
    fl_y=""
    
    def __init__(self,name,level):
        
        if name=="":
            raise ValueError("name cannot be empty")
        else:    
            self._name=name
        if level<=0:
            raise ValueError("level should be > 0")
        else:    
            self._level=level
        
    def __str__(self):
        
        if self.level>0:
            return "{} - Level {}".format(self._name,self._level)
            
    @property
    def name(self):
        return self._name
        
    @property    
    def level(self):
        return self._level
        
        
    @classmethod
    def make_sound(cls):
        print(cls.soun_d)
    
    @classmethod    
    def run(cls):
        print(cls.ru_n)
    
    @classmethod
    def swim(cls):
        print(cls.swi_m)
    
    @classmethod
    def fly(cls):
        print(cls.fl_y)

    
    
class Pikachu(Pokemen):
    
    soun_d="Pika Pika"
    ru_n="Pikachu running..."
    
    def attack(self):
        if self._level==1:
            print("Electric attack with 10 damage")
        if self._level>1:
            damage=self.level*10
            print("Electric attack with {} damage".format(damage))
            
    
    
        

class Squirtle(Pokemen):
    
    soun_d="Squirtle...Squirtle"
    ru_n="Squirtle running..."
    swi_m="Squirtle swimming..."
    
    def attack(self):
        if self.level==1:
            print("Water attack with 9 damage")
        if self.level>1:
            damage=self.level*9
            print("Water attack with {} damage".format(damage))
    
    

class Pidgey(Pokemen):
    
    soun_d="Pidgey...Pidgey"
    fl_y="Pidgey flying..."
        
    
    def attack(self):
        if self.level==1:
            print("Air attack with 5 damage")
        if self.level>1:
            damage=self.level*5
            print("Air attack with {} damage".format(damage))
            
        
class Swanna(Pokemen):
    
    soun_d="Swanna...Swanna"
    fl_y="Swanna flying..."
    swi_m="Swanna swimming..."
    
    def attack(self):
        if self.level==1:
            print("Water attack with 9 damage")
            print("Air attack with 5 damage")
        if self.level>1:
            damage=self.level*9
            damage1=self.level*5
            print("Water attack with {} damage".format(damage))
            print("Air attack with {} damage".format(damage1))
            
    
class Zapdos(Pokemen):
    
    soun_d="Zap...Zap"
    fl_y="Zapdos flying..."
    
    def attack(self):
        if self.level==1:
            print("Electric attack with 10 damage")
            print("Air attack with 5 damage")
        if self.level>1:
            damage=self.level*10
            damage1=self.level*5
            print("Electric attack with {} damage".format(damage))
            print("Air attack with {} damage".format(damage1))
            
            
            
            
    
class Island:
    
    pokemon_list=[]
    island_list=[]
    
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.island_list.append(self)
    
        
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
        
    @property    
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    
    @property    
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property    
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    
    def add_pokemon(self,pokemon):
        if self._max_no_of_pokemon>self._pokemon_left_to_catch:
            self.pokemon_list.append(pokemon)
            self._pokemon_left_to_catch+=1
            
        else:
            print("Island at its max pokemon capacity")
    
    @classmethod        
    def get_all_islands(cls):
        return cls.island_list
            
            
        
class Trainer:
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=10*self._experience
        self._food_in_bag=0
        self._current_island=None
        self._is_an_island=False
        self.pokemons_list=[]
    
    
    @property    
    def name(self):
        return self._name
    
    @property    
    def experience(self):
        return self._experience
    
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    @property    
    def food_in_bag(self):
        return self._food_in_bag
    
    @property
    def current_island(self):
        if self._current_island==None:
            print("You are not on any island")
        else:
            return self._current_island
             
    def move_to_island(self,island):
        self._is_an_island=True
        self._current_island=island
            
               
    
    def collect_food(self):
        if self._is_an_island==True:
            if self._food_in_bag == self._max_food_in_bag:
                pass
            elif self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
                self._food_in_bag += self._max_food_in_bag
                self._current_island._total_food_available_in_kgs-=self._food_in_bag
            else:
                self._food_in_bag +=self._current_island.total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs=0
        else:
            print("Move to an island to collect food")
                
            
    def catch(self,pokemon):
        if self._experience >=100*pokemon.level:
            print('You caught {}'.format(pokemon.name))
            self._experience+=pokemon.level*20
            self.pokemons_list.append(pokemon)
            pokemon._master=self
        else:
            print('You need more experience to catch {}'.format(pokemon.name))
            
        
    def get_my_pokemon(self):
        return self.pokemons_list
        
        
    
        
        
        
    
#island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
#island.name
    