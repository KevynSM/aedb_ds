from tad_list import List
from nodes import SingleListNode

class SingleLinkedList(List):
    def __init__(self):
        self.head = None          
        self.tail = None
        self.length = 0

    
    # Returns true if the list contains no elements.    
    def is_empty(self): # Done
        return self.tail == None


    # Returns the number of elements in the list.    
    def size(self): # Done
        return self.length
        

    # Returns the first element of the list.
    # Throws EmptyListException.    
    def get_first(self): # Done
        if self.length == 0:
            pass #EmptyListException.
        else:
            return self.head.get_element()


    # Returns the last element of the list.
    # Throws EmptyListException.    
    def get_last(self): # Done
        if self.length == 0:
            pass #EmptyListException.
        else: 
            return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): # Done
        var = self.head
        for i in range(0,self.length):            
            if i == position:
                return var.get_element()

            var = var.get_next()
                

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.    
    def find(self, element): # Done
        var = self.head
        for i in range(0,self.length):
            if var.get_element() == element:
                return i
            
           var = var.get_next()
        return -1

    # Inserts the specified element at the first position in the list.    
    def insert_first(self, element): # Done
        element_node = SingleListNode(element, None)

        if self.length == 0:
            self.head = element_node
            self.tail = self.head
        else:
            element_node.set_next(self.head)
            self.head = element_node

        self.length += 1

    # Inserts the specified element at the last position in the list.    
    def insert_last(self, element): # Done
        element_node = SingleListNode(element, None)

        if self.length == 0:
            self.head = element_node
            self.tail = self.head
        else:
            self.tail.set_next(element_node)
            self.tail = element_node

        self.length += 1


    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.    
    def insert(self, element, position):
        if position < 0 or position > self.length: pass #InvalidPositionException
        if position == 0:
            insert_first(element)
        elif position == self.length:
            insert_last(element)
        else:
            element_node = SingleListNode(element, None)
            var = self.head
            for i in range(0,self.length):
                if i == position:

                var = var.get_next()



        

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.    
    def remove_first(self): # Done
        if self.length == 0: pass # EmptyListException.

        first = self.head
        self.head = self.head.get_next()

        self.length -= 1
        return first

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.    
    def remove_last(self):         
        last = self.tail
        var = self.head
        for i in range(0,self.length+1):
            if i == self.length - 1: #penultimo vira ultimo
                self.tail = var
            var = var.get_next()
        self.length -= 1
        return last


    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.    
    def remove(self, position): 
        self.length -= 1

    # Removes all elements from the list.    
    def make_empty(self): 
        self.Head = None
        self.tail = None
        self.length = 0

    # Returns an iterator of the elements in the list (in proper sequence).    
    def iterator(self): pass
