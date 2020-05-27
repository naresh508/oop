import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        
        if type(real_part)==str and type(imaginary_part)==str:
            raise ValueError("Invalid value for real and imaginary part")
        
        if type(real_part)==str:
            raise ValueError("Invalid value for real part")
        else:    
            self._real_part=real_part    
        
        if type(imaginary_part)==str:
            raise ValueError("Invalid value for imaginary part")
        else:    
            self._imaginary_part=imaginary_part
    
    @property        
    def real_part(self):
        return self._real_part
    
    @property    
    def imaginary_part(self):
        return self._imaginary_part
    
    
    def __str__(self):
        if self._imaginary_part<0:
            return "{}-{}i".format(self._real_part,self._imaginary_part)
        else:
            return "{}+{}i".format(self._real_part,self._imaginary_part)
    
    def conjugate(self):
        if self._imaginary_part<0:
            return ComplexNumber(self.real_part,-self._imaginary_part)
        else:
            return ComplexNumber(self.real_part,-self._imaginary_part)
    
    
    def __add__(self,other):
        return ComplexNumber(self._real_part+other._real_part,self._imaginary_part+other._imaginary_part)
    
    
    def __sub__(self,other):
        return ComplexNumber(self._real_part-other._real_part,self._imaginary_part-other._imaginary_part)
        
    
    def __mul__(self,other):
        realpart=(self._real_part*other._real_part)-(self._imaginary_part*other._imaginary_part)
        imaginarypart=(self._imaginary_part*other._real_part)+(self._real_part*other._imaginary_part)
        return ComplexNumber(realpart,imaginarypart)
    
    def __truediv__(self,other):
        R=(self._real_part*other._real_part)+(self.imaginary_part*other._imaginary_part)
        I=(self._imaginary_part*other._real_part)-(self._real_part*other.imaginary_part)
        k=math.pow(other._real_part,2)+math.pow(other._imaginary_part,2)
        return ComplexNumber(R/k,I/k)
        
    def __abs__(self):
       k=math.sqrt(math.pow(self.real_part,2)+math.pow(self.imaginary_part,2))
       return abs(round(k,3))
       
    def __eq__(self,other):
        if self._real_part==other._real_part and self._imaginary_part==other._imaginary_part:
            return True
        else:
            return False