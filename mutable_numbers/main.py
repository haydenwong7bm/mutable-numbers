from numbers import *
import math
from copy import deepcopy

class MutableInt(Integral):
    def __init__(self, x=0):
        if type(x) == __class__:
            return x.copy()
        
        x = int(x)
        
        if x < 0:
            self.__negative = True
        else:
            self.__negative = False
        
        x = abs(x)
        
        self.__data = set()
        
        n = 0
        while x:
            if x & 1:
                self.__data.add(n)
            x >>= 1
            n += 1
            
    def __complex__(self):
        return complex(int(self))
        
    def __bool__(self):
        return bool(int(self))
        
    def real(self):
        return __class__(int(self).real())
        
    def imag(self):
        return __class__(int(self).imag())
        
    def __add__(self, other):
        return __class__(int(self) + int(other))
        
    def __pos__(self):
        return self
        
    def __sub__(self, other):
        return __class__(int(self) - int(other))
        
    def __neg__(self):    
        return __class__(-int(self))
        
    def __mul__(self, other):
        return __class__(int(self) * int(other))
        
    def __truediv__(self, other):
        return MutableFloat(int(self) / int(other))
        
    def __radd__(self, other):
        return __class__(int(other) + int(self))
        
    def __rsub__(self, other):
        return __class__(int(other) - int(self))
        
    def __rmul__(self, other):
        return __class__(int(other) * int(self))
        
    def __rtruediv__(self, other):
        return MutableFloat(int(other) // int(self))
        
    def __abs__(self, other):
        return __class__(abs(int(self)))
        
    def conjugate(self):
        return __class__(int(self).conjugate())
        
    def __eq__(self, other):
        return int(self) == int(other)
        
    def __ne__(self, other):
        return int(self) != int(other)
        
    def __float__(self):
        return float(int(self))
        
    def __trunc__(self):
        return __class__(math.trunc(int(self)))
        
    def __round__(self, ndigits=None):
        return __class__(round(int(self), ndigits))
        
    def __floor__(self):
        return __class__(math.floor(int(self)))
        
    def __ceil__(self):
        return __class__(math.ceil(int(self)))
        
    def __divmod__(self, other):
        return (self // other, self % other)
        
    def __floordiv__(self, other):
        return __class__(int(self) // int(other))
        
    def __mod__(self, other):
        return __class__(int(self) % int(other))
        
    def __rfloordiv__(self, other):
        return __class__(int(other) // int(self))
        
    def __rmod__(self, other):
        return __class__(int(other) % int(self))
        
    def __lt__(self, other):
        return int(self) < int(other)
        
    def __le__(self, other):
        return int(self) <= int(other)
        
    def __gt__(self, other):
        return int(self) > int(other)
        
    def __ge__(self, other):
        return int(self) >= int(other)
        
    def numerator(self):
        return __class__(int(self).numerator)
        
    def denominator(self):
        return __class__(int(self).denominator)
        
    def __int__(self):
        return sum(1 << n for n in self.__data)
        
    def __pow__(self, other, modulo=None):
        return pow(int(self), int(other), int(modulo))
        
    def __lshift__(self, other):
        return __class__(int(self) << int(other))
        
    def __rshift__(self, other):
        return __class__(int(self) >> int(other))
        
    def __and__(self, other):
        return __class__(int(self) & int(other))
        
    def __xor__(self, other):
        return __class__(int(self) ^ int(other))
        
    def __or__(self, other):
        return __class__(int(self) | int(other))
        
    def __rpow__(self, other):
        return pow(int(other), int(self))
        
    def __rlshift__(self, other):
        return __class__(int(other) << int(self))
        
    def __rrshift__(self, other):
        return __class__(int(other) >> int(self))
        
    def __rand__(self, other):
        return __class__(int(other) & int(self))
        
    def __rxor__(self, other):
        return __class__(int(other) ^ int(self))
        
    def __ror__(self, other):
        return __class__(int(other) | int(self))
    
    def __invert__(self):
        return __class__(~int(self))
    
    def copy(self):
        return deepcopy(self)