from tad_list import List
from nodes import DoubleListNode
from tad_iterator import Iterator
from exceptions import EmptyListException, InvalidPositionException, NoSuchElementException

class DoublyLinkedList(List):
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
            raise EmptyListException()
        else:
            return self.head

    # Returns the last element of the list.
    # Throws EmptyListException.    
    def get_last(self): # Done
        if self.length == 0:
            raise EmptyListException()
        else: 
            return self.tail

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): # Done
        if position < 0 or position > self.length-1: raise InvalidPositionException()
        middle = int(self.length/2)
        if position < middle:
            var = self.head
            for i in range(0, middle):
                if i == position:
                    return var
                
                var = var.get_next()
        else:
            var = self.tail
            for i in range(self.length,middle-1,-1):
                if i == position:
                    return var

                var = ver.get_previous()
                
    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.    
    def find(self, element): # Done
        var = self.head
        element_node = DoubleListNode(element, None, None)
        for i in range(0,self.length):
            if var == element_node:
                return i
            
           var = var.get_next()
        return -1

    # Inserts the specified element at the first position in the list.    
    def insert_first(self, element): 
        element_node = DoubleListNode(element, None, None)

        if self.length == 0:
            self.head = element_node
            self.tail = self.head
        else:
            element_node.set_next(self.head)
            self.head.set_previous(element_node)
            self.head = element_node

        self.length += 1

    # Inserts the specified element at the last position in the list.    
    def insert_last(self, element): # Done
        element_node = DoubleListNode(element, None, None)

        if self.length == 0:
            self.head = element_node
            self.tail = self.head
        else:
            self.tail.set_next(element_node)
            element_node.set_previous(self.tail)
            self.tail = element_node

        self.length += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.    
    def insert(self, element, position): #Done
        if position < 0 or position > self.length: raise InvalidPositionException()
        if position == 0:
            insert_first(element)
        elif position == self.length:
            insert_last(element)
        else:
            element_node = DoubleListNode(element, None, None)
            var = get(position - 1)
            temp = var.get_next()

            var.set_next(element_node)
            element_node.set_previous(var)

            element_node.set_next(temp)
            temp.set_previous(element_node)

            self.length += 1
        
    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.    
    def remove_first(self): # Done
        if self.length == 0: raise EmptyListException()

        first = self.head
        self.head = self.head.get_next()
        self.head.set_previous(None)


        self.length -= 1
        return first

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.    
    def remove_last(self): # Done      
        if self.length == 0: raise EmptyListException()
        removed = self.tail 
        self.tail = sel.tail.get_previous()
        self.tail.set_next(None)


        self.length -= 1
        return removed
        
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.    
    def remove(self, position): # Done
        if position < 0 or position > self.length: raise InvalidPositionException()
        if position == 0:
            remove_first()
        elif position == self.length:
            remove_last()
        else:
            removed = get(position)
            removed.get_previous().set_next(removed.get_next())
            removed.get_next().set_previous(removed.get_previous())           

            self.length -= 1
            return removed

    # Removes all elements from the list.    
    def make_empty(self): # Done
        self.Head = None
        self.tail = None
        self.length = 0

    # Returns an iterator of the elements in the list (in proper sequence).    
    def iterator(self): 
        i = l.Iterator()
        while i.has_next():
            e = i.next()