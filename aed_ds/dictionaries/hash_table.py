from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item 

import ctypes 

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        self.table = (self.array_size * ctypes.py_object)() # Array of pointers

        # Create an empty list for each table position
        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size

    def get(self, k): 
        if not(self.has_key(k)):
            raise NoSuchElementException()
        idx = self.hash_function(k)

        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return current_item.get_value()

        


    def insert(self, k, v):
        # Check if it has key
        if self.has_key(k):
            raise DuplicatedKeyException()

        ## Insert new item
        # Calculate the table index
        idx = self.hash_function(k) # O(1)
        # Create a new Item
        item = Item(k, v)
        # Insert the item in the colision list
        self.table[idx].insert_last(item)
        # Update the number of elements
        self.num_elements += 1    

    def update(self, k, v): 
        if not(self.has_key(k)):
            raise NoSuchElementException()

        idx = self.hash_function(k)

        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                current_item.set_value(v)
                break

        

    def remove(self, k):
        if not(self.has_key(k)):
            raise NoSuchElementException()
        
        idx = self.hash_function(k)

        colision_list = self.table[idx]
        
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                position = colision_list.find(current_item)
                colision_list.remove(position)
                self.num_elements -= 1    
                return current_item.get_value()
        
        
        
            

    def keys(self): 
        list_keys = SinglyLinkedList()

        for i in range(self.array_size):
            colision_list = self.table[i]
            colision_size = colision_list.size()
            for j in range(colision_size):
                list_keys.insert_last(colision_list.get(j).get_key())
                

        return list_keys

    def values(self): 
        list_values = SinglyLinkedList()

        for i in range(self.array_size):
            colision_list = self.table[i]
            colision_size = colision_list.size()
            for j in range(colision_size):
                list_values.insert_last(colision_list.get(j).get_value())

        return list_values

    def items(self): 
        list_itens = SinglyLinkedList()

        for i in range(self.array_size):
            colision_list = self.table[i]
            colision_size = colision_list.size()
            for j in range(colision_size):
                list_itens.insert_last(colision_list.get(j))

        return list_itens

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.array_size

    def has_key(self, k):
        idx = self.hash_function(k) # O(1)    
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return True
        return False