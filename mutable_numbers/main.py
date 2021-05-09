from numbers import *
import math
from copy import deepcopy

class MutableInt(Integral):
    """Mutable version of Python's bulit-in int type"""
    
    def __init__(self, x=0):
        if type(x) == __class__:
            return x.copy()
        
        self.__value = int(x)
    
    
    
    # Abstract methods needed to be defined by numbers.Integral
    
    def __complex__(self):
        return complex(self.__value)
        
    def __bool__(self):
        return bool(self.__value)
        
    def real(self):
        return __class__(self.__value.real())
        
    def imag(self):
        return __class__(self.__value.imag())
        
    def __add__(self, other):
        return __class__(self.__value + other.__value)
        
    def __pos__(self):
        return self
        
    def __sub__(self, other):
        return __class__(self.__value - other.__value)
        
    def __neg__(self):    
        return __class__(-self.__value)
        
    def __mul__(self, other):
        return __class__(self.__value * other.__value)
        
    def __truediv__(self, other):
        return MutableFloat(self.__value / other.__value)
        
    def __radd__(self, other):
        return __class__(other.__value + self.__value)
        
    def __rsub__(self, other):
        return __class__(other.__value - self.__value)
        
    def __rmul__(self, other):
        return __class__(other.__value * self.__value)
        
    def __rtruediv__(self, other):
        return MutableFloat(other.__value // self.__value)
        
    def __abs__(self, other):
        return __class__(abs(self.__value))
        
    def conjugate(self):
        return __class__(self.__value.conjugate())
        
    def __eq__(self, other):
        return int(self) == int(other)
        
    def __ne__(self, other):
        return int(self) != int(other)
        
    def __float__(self):
        return float(self.__value)
        
    def __trunc__(self):
        return __class__(math.trunc(self.__value))
        
    def __round__(self, ndigits=None):
        return __class__(round(self.__value, ndigits))
        
    def __floor__(self):
        return __class__(math.floor(self.__value))
        
    def __ceil__(self):
        return __class__(math.ceil(self.__value))
        
    def __divmod__(self, other):
        return (self // other, self % other)
        
    def __floordiv__(self, other):
        return __class__(self.__value // other.__value)
        
    def __mod__(self, other):
        return __class__(self.__value % other.__value)
        
    def __rdivmod__(self, other):
        return (other // self, other % self)
        
    def __rfloordiv__(self, other):
        return __class__(other.__value // self.__value)
        
    def __rmod__(self, other):
        return __class__(other.__value % self.__value)
        
    def __lt__(self, other):
        return int(self) < int(other)
        
    def __le__(self, other):
        return int(self) <= int(other)
        
    def __gt__(self, other):
        return int(self) > int(other)
        
    def __ge__(self, other):
        return int(self) >= int(other)
        
    def numerator(self):
        return __class__(self.__value.numerator)
        
    def denominator(self):
        return __class__(self.__value.denominator)
        
    def __int__(self):
        return self.__value
        
    def __pow__(self, other, modulo=None):
        return pow(self.__value, other.__value, int(modulo))
        
    def __lshift__(self, other):
        return __class__(self.__value << other.__value)
        
    def __rshift__(self, other):
        return __class__(self.__value >> other.__value)
        
    def __and__(self, other):
        return __class__(self.__value & other.__value)
        
    def __xor__(self, other):
        return __class__(self.__value ^ other.__value)
        
    def __or__(self, other):
        return __class__(self.__value | other.__value)
        
    def __rpow__(self, other):
        return pow(other.__value, self.__value)
        
    def __rlshift__(self, other):
        return __class__(other.__value << self.__value)
        
    def __rrshift__(self, other):
        return __class__(other.__value >> self.__value)
        
    def __rand__(self, other):
        return __class__(other.__value & self.__value)
        
    def __rxor__(self, other):
        return __class__(other.__value ^ self.__value)
        
    def __ror__(self, other):
        return __class__(other.__value | self.__value)
    
    def __invert__(self):
        return __class__(~self.__value)
    
    
    
    # Other methods brought from the int type
    
    def __index__(self):
        return self.__value
    
    def __repr__(self):
        return 'MutableInt({})'.format(self.__value)
        
    def __str__(self):
        return str(self.__value)
        
    def bit_length(self):
        return self.__value.bit_length()
        
    def to_bytes(self, length, byteorder, signed=False):
        return self.__value.to_bytes(length, byteorder, signed=False)
        
    def from_bytes(self, bytes, byteorder, signed=False):
        return __class__(int.from_bytes(bytes, byteorder, signed=False))
        
    def as_integer_ratio(self):
        return (self.copy(), __class__(1))
    
    # Other methods
    
    def copy(self):
        return __class__(self.__value)
        
    def __iadd__(self, other):
        self.__value = self.__value + int(other)
        return self
        
    def __isub__(self, other):
        self.__value = self.__value - int(other)
        return self
        
    def __imul__(self, other):
        self.__value = self.__value * int(other)
        return self
        
    def __ifloordiv__(self, other):
        self.__value = self.__value // int(other)
        return self
        
    def __imod__(self, other):
        self.__value = self.__value % int(other)
        return self
        
    def __ipow__(self, other):
        self.__value = self.__value ** int(other)
        return self
        
    def __ilshift__(self, other):
        self.__value = self.__value << int(other)
        return self
        
    def __irshift__(self, other):
        self.__value = self.__value >> int(other)
        return self
        
    def __iand__(self, other):
        self.__value = self.__value & int(other)
        return self
        
    def __ixor__(self, other):
        self.__value = self.__value ^ int(other)
        return self
        
    def __ior__(self, other):
        self.__value = self.__value | int(other)
        return self
    
    def incr(self, value=1):
        self += value
        return self
        
    def decr(self, value=1):
        self -= value
        return self
        
    def __getitem__(self, key):
        return int('{:b}'.format(self.__value)[::-1][key], 2)
        
    def __setitem__(self, key, value):
        length = max(0, (key.stop - key.start + (key.step - (1 if key.step > 0 else -1))) // key.step)
        
        if value < 0:
            value = (1 << length) - abs(value)
        
        data = list(map(bool, '{:b}'.format(self.__value)[::-1]))
        data[key] = list(map(bool, '{:b}'.format(self.__value).zfill(length)[::-1]))
        self.__value = int('{:b}'.format(''.join(data))[::-1], 2)
        return self
        
    def __delitem__(self, key):
        data = list(map(bool, '{:b}'.format(self.__value)[::-1]))
        data[key] = []
        self.__value = int('{:b}'.format(''.join(data))[::-1], 2)
        return self