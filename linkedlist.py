
#creating a class "Node" so as to enable creation of objects
class Node:
    #data means the value currently held in the node
    #next stores the reference to the next node in the list
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class Linked_list:
    #creating a constructor for the node and making it empty
    def __init__(self):
        self.head = None
        self.tail = None
        
    #1st method
    def insert_at_end(self, data):
        #creating a new node object that points to nothing
        new_node = Node(data, None)
        
        #i have created a new object above, meaning there is only 1 possible head and the tail obviously points to none
        
        #If i am dealing with a new node and i add data, that would mean both the tail and head are new
        #only later when i add new nodes is when the tail will change
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        #if there are already nodes in the list, we go to the tail i.e the last and assign it a new node and then
        #the tail now becomes the newly added node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    #2nd method
    def insert_at_start(self, data):
        #Since we are inserting at the head, it should always have something to point to, in this case the original head
        
        new_node = Node(data, self.head)  
        #now the head is the node that i have just created
        self.head = new_node
        
        #to ensire that if the list is empty, the none is assigned the node i have just created
        if self.tail is None:
            self.tail = new_node
            
    
            