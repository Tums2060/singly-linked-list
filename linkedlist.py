
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
            
    #3rd method
    def insert_at_index(self, data, index):
        if (index == 0):
            self.insert_at_start(data)
            return
        elif (index == -1):
            self.insert_at_end(data)
            return
        
        #To keep track of current position in the list
        position = 0
        
        #Starting from the head
        current_node = self.head
        #transversing until the position is last or a position before the index is reached
        
        while (current_node != None and position+1 != index):
            position = position+1
            #We continue moving to the next node in the list until the while loop is satisfied
            current_node = current_node.next
          
        #if the new node index is valid,  
        if current_node != None:
            new_node = Node(data)
        #we create it and make it point to the same value as the current_node
            new_node.next = current_node.next
        #and then i change the current_node to point to the new_node which points to the value after
        #This inserts it between
            current_node.next = new_node
        else:
            print("Index not present")
            
    #4th method
    def delete_at_index(self, index):
        #To check if the list is empty
        if self.head is None:
            return
        
        #If the 1st index is deleted i.e. the head, i assign it to a variable
        if index == 0:
            deleted_node = self.head
            #And the i make the new head the one which the orignal head was pointing to
            self.head = self.head.next
            return
        
        #initializing a counter and starting from the head
        position = 0
        current_node = self.head
        
        #It continues transversing until it reaches the end, or the node before the index
        while current_node.next is not None and position+1 < index:
            position = position+1
            #Moving to next node while true
            current_node = current_node.next
        #If index is higher and it loops till it reaches the end
        if current_node.next is None:
            print("Index out of bounds")
        #Assigning the current_node.next to be deleted, as we have stopped at current_node
        else:
            deleted_node = current_node.next
            #Skipping past the deleted node
            current_node.next = current_node.next.next
    
    #5th method        
    def search(self, data):
        #Starting at the begining of the list
        current_node = self.head
        #creating the variavle index and assigning it 0
        index =0
        
        while current_node != None:
            #If the current nodes data is equal to the data we return the count of the index
            if current_node.data == data:
                return index
            #If not we go to the next node and increment index until the data is equal to what was inputted
            current_node = current_node.next
            index = index +1
            #If it doesn't exist, we return -1
            return -1
    
    #6th method
    def display(self):
        #Starting from the head
        current_node = self.head
        #print all values one by one going to the next
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
        
##IMPLEMENTING THE FUNCTIONS
l1 = Linked_list()
l1.insert_at_start('a')
l1.insert_at_end('b')

l1.insert_at_index('c',0)

l1.display()

print(l1.search('c'))
            
            