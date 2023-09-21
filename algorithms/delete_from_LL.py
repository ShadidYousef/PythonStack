# check if LL is empty or not 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

  #Add new element at the tail of the list
    def AddELement(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        return self

  #display the values of the list
    def PrintList(self):
        temp = self.head
        if temp != None:
            print("The list contains:")
            while temp != None:
                print(temp.data ,"---->")
                temp = temp.next
        else:
            print("The list is empty.")
        return self
    #delete a node at a given position from the LL
    def delete_from_LL(self, position):
        if position == 0:
            return self.head.next
        else:
            for i in range(position-1):
                CurrentNode = CurrentNode.next
            CurrentNode = CurrentNode.next.next
        return self
            

MyList = LinkedList()
#Add four elements at the end of the list.
MyList.AddELement(10).AddELement(20).AddELement(30).AddELement(30).PrintList()
# MyList.delete_from_LL(1)
# MyList.PrintList()
