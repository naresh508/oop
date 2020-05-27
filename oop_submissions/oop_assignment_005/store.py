class Item:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        if self.price<=0:
            raise ValueError("Invalid value for price, got {}".format(self.price))
        self.category=category
    
    def __str__(self):
        return '{}@{}-{}'.format(self.name,self.price,self.category)

class Query:
    def __init__(self,field,operation,value):
        self.field=field
        l=["IN","EQ","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
        if operation in l:
            self.operation=operation
        else:
            raise ValueError("Invalid value for operation, got random")
        
        self.value=value
    
    def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)

class Store:
    def __init__(self):
        self.list_item=[]
    def add_item(self,item):
        self.list_item.append(item)
    def __str__(self):
        if len(self.list_item)>0:
            return '\n'.join(map(str, self.list_item))
        else:
            "No items"
    def count(self):
        return len(self.list_item)
            
    def filter(self,query):
        object =Store()
        for i in self.list_item:
            if query.operation=="IN" and getattr(i,query.field) in query.value:
                object.add_item(i)
            elif query.operation=="EQ" and getattr(i,query.field) == query.value:
                object.add_item(i)
            elif query.operation=="GT" and getattr(i,query.field) > query.value:
                object.add_item(i)
            elif query.operation=="GTE" and getattr(i,query.field) >= query.value:
                object.add_item(i)    
            elif query.operation=="LT" and getattr(i,query.field) < query.value:
                object.add_item(i)
            elif query.operation=="LTE" and getattr(i,query.field) <= query.value:
                object.add_item(i)
            elif query.operation=="STARTS_WITH" and query.value in getattr(i,query.field):
                object.add_item(i)
            elif query.operation=="ENDS_WITH" and query.value in getattr(i,query.field):
                object.add_item(i)
            elif query.operation=="CONTAINS" and query.value in getattr(i,query.field):
                object.add_item(i)
        return object      
    def exclude(self,query):
        object1=Store()
        k=self.filter(query)
        for i in self.list_item:
            if i not in self.list_item:
                object1.add_item(i)
        return object1
            
            
        
        '''#object=Store()
        self.list=[]
        if query.operation=="IN":
            for i in self.list_item:
                if i.name in query.value:
                    self.list.append(i)
                    #object.add_item
                elif i.price in query.value:
                    self.list.append(i)
                    #object.add_item
                elif i.category in query.value:
                    self.list.append(i)
                    #object.add_item
            #return '\n'.join(map(str,self.list))                    
        
        if query.operation=="EQ":
            for i in self.list_item:
                if i.name==query.value:
                    self.list.append(i)
                    #object.add_item
                elif i.price==query.value:
                    self.list.append(i) 
                    #object.add_item
                elif i.category==query.value:
                    self.list.append(i)
                    #object.add_item
            #return '\n'.join(map(str,self.list))            
        
        elif query.operation=="GT":
            for i in self.list_item:
                if i.price>query.value:
                    self.list.append(i)
                    #object.add_item
            #return '\n'.join(map(str,self.list)) 
        
        elif query.operation=="GTE":
            for i in self.list_item:
                if i.price>=query.value:
                    self.list.append(i)
                    #object.add_item
            #return '\n'.join(map(str,self.list))         
        
        elif query.operation=="LT":
            for i in self.list_item:
                if i.price<query.value:
                    self.list.append(i)
                    #object.add_item
            #return '\n'.join(map(str,self.list))         
        
        elif query.operation=="LTE":
            for i in self.list_item:
                if i.price<=query.value:
                    self.list.append(i)
                    #object.add_item
            #return '\n'.join(map(str,self.list))                 
                    
        elif query.operation=="STARTS_WITH":
            for i in self.list_item:
                if query.field=="name" or query.field=="category":
                    if  i.name.startswith(query.value):
                        self.list.append(i)
                        #object.add_item
                    elif  i.category.startswith(query.value):
                        self.list.append(i)    
                        #object.add_item
            #return '\n'.join(map(str,self.list))     
                    
        elif query.operation=="ENDS_WITH":
            for i in self.list_item:
                if query.field=="name" or query.field=="category":
                    if  i.name.endswith(query.value):
                        self.list.append(i)
                        #object.add_item
                    elif  i.category.endswith(query.value):
                        self.list.append(i)    
                        #object.add_item
            #return '\n'.join(map(str,self.list))
                    
        elif query.operation=="CONTAINS":
            for i in self.list_item:
                if query.field=="name" or query.field=="category":
                    if i.name.__contains__(query.value):
                        self.list.append(i)
                        #object.add_item
                    elif i.category.__contains__(query.value):
                        self.list.append(i)
                        #object.add_item
        return '\n'.join(map(str,self.list))
        #return object.add_item
        
    def exclude(self,query):
        list=Store()
        if query.operation=="IN":
            for i in self.list_item:
                if  i.name not in query.value:
                    self.list.append(i)
                elif i.price not in query.value:
                    self.list.append(i) 
                elif i.category not in query.value:
                    self.list.append(i)
        
        if query.operation=="EQ":
            for i in self.list_item:
                if not i.name==query.value:
                    self.list.append(i)
                elif not  i.price!=query.value:
                    self.list.append(i) 
                elif not i.category!=query.value:
                    self.list.append(i) 
        
        elif query.operation=="GT":
            for i in self.list_item:
                if not (i.price>query.value):
                    self.list.append(i) 
            return '\n'.join(map(str,self.list))                  
        
        elif query.operation=="GTE":
            for i in self.list_item:
                if not (i.price>=query.value):
                    self.list.append(i)
        
        elif query.operation=="LT":
            for i in self.list_item:
                if not (i.price<query.value):
                    self.list.append(i) 
        
        elif query.operation=="LTE":
            for i in self.list_item:
                if not (i.price<=query.value):
                    self.list.append(i)  
                    
        elif query.operation=="STARTS_WITH":
            for i in self.list_item:
                if query.field!="name" or query.field!="category":
                    if not i.name.startswith(query.value):
                        self.list.append(i)
                    if not i.category.startswith(query.value):
                        self.list.append(i) 
        elif query.operation=="ENDS_WITH":
            for i in self.list_item:
                if query.field!="name" or query.field!="category":
                    if not  i.name.endswith(query.value):
                        self.list.append(i)
                        #object.add_item
                    elif not  i.category.endswith(query.value):
                        self.list.append(i)   
                        
        elif query.operation=="CONTAINS":
            for i in self.list_item:
                if query.field=="name" or query.field=="category":
                    if  not i.name.__contains__(query.value):
                        self.list.append(i)
                        #object.add_item
                    elif not i.category.__contains__(query.value):
                        self.list.append(i)'''               
                        
            
            
            
            
            
            
                
            
                    
                
                    
                
        
        





#store = Store()  
#item = Item(name="Oreo Biscuits", price=30, category="Food")  
#store.add_item(item)  
#item = Item(name="Boost Biscuits", price=20, category="Food")  
#store.add_item(item)  
#item = Item(name="Butter", price=10, category="Grocery")  
#store.add_item(item)  
#query = Query(field="category", operation="IN", value=["Food"])  
#results = store.filter(query)  
#print(results)
#store = Store()  
#item = Item(name="Oreo Biscuits", price=30, category="Food")  
#store.add_item(item)  
#item = Item(name="Boost Biscuits", price=20, category="Food")  
#store.add_item(item)  
#print(store)  
#store = Store()  
#item = Item(name="Oreo Biscuits", price=30, category="Food")  
#store.add_item(item)  
#item = Item(name="Boost Biscuits", price=20, category="Food")  
#store.add_item(item)  
#query = Query(field="price", operation="LTE", value=20)  
#results = store.filter(query) 
#print(results) 
#query = Query(field="price", operation="LT", value=20)  
#results = store.filter(query) 
#print(results)  
#store.add_item(item)  
#query = Query(field="category", operation="IN", value=["Food"])  
#results = store.filter(query)  
#print(results) 
#query1 = Query(field="price", operation="GT", value=20)  
#results = store.filter(query1) 
#print(results) 
#query2 = Query(field="name", operation="ENDS_WITH", value="cuits")  
#results = store.filter(query2) 
#print(results)
#query3 = Query(field="name", operation="CONTAINS", value="uit")  
#results = store.filter(query3) 
#print(results)
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="ParleG Biscuits", price=10, category="Food")  
store.add_item(item) 
print(store)

            
    


        
#def filter(list_items,item):
    #for x in range(len(list_items)):
        #y=x[0]
        
        #if item in list_items:
            #return True
        #else:
            #return False

            
        
                
            
            
            
        

        
    