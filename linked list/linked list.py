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
      while(current.next != None):
        current = current.next
      current.next = newNode

  #display the values of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:")
      while (temp != None):
        print(temp.data ,"---->")
        temp = temp.next
      
    else:
      print("The list is empty.")
                  
MyList = LinkedList()
#Add four elements at the end of the list.
MyList.AddELement(10)
MyList.AddELement(20)
MyList.AddELement(30)
MyList.AddELement(30)
MyList.PrintList()