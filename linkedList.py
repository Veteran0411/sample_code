class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    def __init__(self):
        self.head=None
    
    def insertFirst(self,data):
        new_node=Node(data)
        new_node.next=self.head 
        self.head=new_node
        
    def insert_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            print("value added at last")
            return
        curr=self.head
        while(curr.next is not None):
            curr=curr.next
        curr.next=new_node
        
            
    def print_list(self):
        if self.head is None:
            print("list is empty") 
            return
        else:
            curr=self.head
            while(curr is not None):
                print(curr.data,end="->")
                curr=curr.next
                    
if __name__=="__main__":
    l1=LinkedList()
    while True:
        n=int(input("enter your choice"))
        match n:
            case 1: l1.insertFirst(input("enter the value to insert"))
            case 2: l1.insert_last(input("enter the value to insert"))
            case 3: l1.print_list()
            case 4: exit()
    
        