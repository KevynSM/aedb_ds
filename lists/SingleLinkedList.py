from tad_list import List
from nodes import SingleListNode

class SingleLinkedList(List):
    def __init__(self):
        self.head = None          
        self.tail = None
        self.element_count = 0
               
    
    
    # Returns true if the list contains no elements.    
    def is_empty(self): 
        return self.tail == None


    # Returns the number of elements in the list.    
    def size(self): 
        return self.element_count
        

    # Returns the first element of the list.
    # Throws EmptyListException.    
    def get_first(self):
        if self.head == None:
            pass #EmptyListException.
        else:
            return self.head.get_element()


    # Returns the last element of the list.
    # Throws EmptyListException.    
    def get_last(self):
        if self.tail == None:
            pass #EmptyListException.
        else: 
            return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): 
        var = self.head
        for i in range(0,self.element_count+1):            
            if i == position:
                return var.get_element()

            var = var.get_next()
                

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.    
    def find(self, element): 
        var = self.head
        for i in range(0,self.element_count+1):
            if var.get_element() == element:
                return i
            
           var = var.get_next()

    # Inserts the specified element at the first position in the list.    
    def insert_first(self, element): 
        self.element_count += 1
        element.set_next(self.head)
        self.head = element

    # Inserts the specified element at the last position in the list.    
    def insert_last(self, element): 
        self.element_count += 1
        self.tail.set_next(element)
        self.tail = element


    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.    
    def insert(self, element, position): 
        var = self.head
        if position > self.element_count:
            pass #InvalidPositionException 
        else:
            self.element_count += 1
            for i in range(0,self.element_count+1):
                if i == position - 1:
                    varset_next(element)
                if i == position:
                    temp = var
                    var = element
                    var.set_next(temp)

                var = var.get_next()

        

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.    
    def remove_first(self): 
        self.element_count -= 1
        first = self.head
        self.head = self.head.get_next()
        return first

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.    
    def remove_last(self):         
        last = self.tail
        var = self.head
        for i in range(0,self.element_count+1):
            if i == self.element_count - 1: #penultimo vira ultimo
                self.tail = var
            var = var.get_next()
        self.element_count -= 1


    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    
    def remove(self, position): 
        self.element_count -= 1

    # Removes all elements from the list.    
    def make_empty(self): 
        self.Head = None
        self.tail = None
        self.element_count = 0

    # Returns an iterator of the elements in the list (in proper sequence).    
    def iterator(self): pass
