from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import DuplicatedKeyException, NoSuchElementException, EmptyTreeException, \
    EmptyDictionaryException
from .nodes.binary_nodes import BinarySearchTreeNode


class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self):
        self.root = None
        self.num_elements = 0

    # Returns the number of elements in the dictionary.
    def size(self): 
        return self.num_elements

    # Returns true if the dictionary is full.
    def is_full(self): 
        return False

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):
        return self.get_aux(self.root, k).get_element()

    def get_aux(self, root, k):
        if root is None:
            raise NoSuchElementException()
        else:
            if root.get_key() == k:
                return root
            elif root.get_key() > k:
                root = self.get_aux(root.get_left_child(), k)
            elif root.get_key() < k:
                root = self.get_aux(root.get_right_child(), k)
        return root
         


    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v): 
        self.root = self.insert_element(self.root, k, v)

    def insert_element(self, root, k, v):
        if root is None:
            root = BinarySearchTreeNode(k, v)
            self.num_elements += 1
        else:
            if root.get_key() == k:
                raise DuplicatedKeyException()
            elif root.get_key() > k:
                node = self.insert_element(root.get_left_child(), k , v)
                root.set_left_child(node)
            else:
                node = self.insert_element(root.get_right_child(), k , v)
                root.set_right_child(node)
        return root


    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): 
        current_node = self.root
        while True:
            if current_node.get_key() == k:
                current_node.set_element(v)
                break
            elif current_node.get_key() > k:
                current_node = current_node.left_child                
            elif current_node.get_key() < k:
                current_node = current_node.right_child
                
   
    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k):
        self.root = self.remove_aux(self.root, k)
        self.num_elements -= 1


    def remove_aux(self, root, k):
        if root is None:
            raise NoSuchElementException()
        else:
            if root.is_leaf():
                if self.get_father(root, k).get_left_child().get_key() == k:
                    self.get_father(root, k).set_left_child(None)
                elif self.get_father(root, k).get_right_child().get_key() == k:
                    self.get_father(root, k).set_right_child(None)
                #return root
            elif root.get_right_child() == None:
                root = root.get_left_child()
                #return root
            elif root.get_left_child() == None:
                # looking for the new root
                new_root = self.get_min_node(root.get_right_child())
                # remove the new root for the old position
                self.get_father(root, new_root.get_key()).set_left_child(None)
                # copy the child
                new_root.set_right_child(root.get_right_child())
                # set the root to be the new root
                root = new_root
                #return root
            
            else:
                if root.get_key() < k:
                    root = self.remove_aux(root.get_left_child(), k)
                elif root.get_key() > k:
                    root = self.remove_aux(root.get_right_child(), k)
        return root

    
  
    def get_father(self, root, k):
        if root.get_right_child().get_key() == k or root.get_left_child().get_key() == k:
            return root        
        else:
            if root.get_key() > k:
                self.get_father(root.left_child(), k)                
            elif root.get_key() < k:
                self.get_father(root.right_child(), k)


    


    # Returns a List with all the keys in the dictionary.
    def keys(self): 
        list_keys = SinglyLinkedList()
        self.infixo_keys(self.root, list_keys)
        return list_keys

    def infixo_keys(self, root, list):
        if root != None:
            self.infixo_keys(root.get_left_child(), list)
            list.insert_last(root.get_key())
            self.infixo_keys(root.get_right_child(), list)
    
    # Returns a List with all the values in the dictionary.
    def values(self): 
        list_values = SinglyLinkedList()
        self.infixo_values(self.root, list_values)
        return list_values

    def infixo_values(self, root, list):
        if root != None:
            self.infixo_values(root.get_left_child(), list)
            list.insert_last(root.get_element())
            self.infixo_values(root.get_right_child(), list)

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): 
        list_items = SinglyLinkedList()
        self.infixo_items(self.root, list_items)
        return list_items

    def infixo_items(self, root, list):
        if root != None:
            self.infixo_items(root.get_left_child(), list)
            list.insert_last(root)
            self.infixo_items(root.get_right_child(), list)


    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass
        

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self): 
        if self.is_empty():
            raise EmptyTreeException()
        return self.get_min_node(self.root).get_element()        
    
    def get_min_node(self, root):
        if root.get_left_child() is None:
            return root
        return self.get_min_node(root.get_left_child())

    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self):
        if self.is_empty():
            raise EmptyTreeException()
        return self.get_max_node(self.root).get_element()

    def get_max_node(self, root):
        if root.get_right_child() is None:
            return root
        return self.get_max_node(root.get_right_child())

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self): 
        if self.is_empty():
            raise EmptyTreeException()
        return self.root

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self): pass

    # Returns True if the tree is empty
    def is_empty(self): 
        return self.num_elements == 0
    