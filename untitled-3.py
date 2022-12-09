class Queue:
    def __init__(self):
        self.mylist = []
        pass    
    def enqueue(self, input):
        self.mylist.append(input)

    def pick(self):
        a = self.mylist[0]
        self.mylist.pop(0)
        return a

    def dequeue(self,input):
        self.mylist=[input]+self.mylist
        pass

