from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item
import ctypes

class HashTable(Dictionary):
    def __init__(self, size=101):       
       self.elements = 0
       self.max_elements = size
       idx_array = (self.max_elements * ctypes.py_object)()

    def size(self):
        return self.elements

    def is_full(self):
        return self.max_elements == self.elements

    def get(self, k): pass


    def insert(self, k, v): 
        idx = hash(k,self.max_elements)
        if type(k) == "int":
            idx = k % self.max_elements
        elif type(k) == "str":
            idx = sum(ord(c))
        new_item = Item(k,v)
        idx_array[idx] = 


    def update(self, k, v): pass

    def remove(self, k): pass

    def keys(self): pass

    def values(self): pass

    def items(self): pass