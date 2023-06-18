class Queue1:

    def __init__(self):
        self.queue=[]

    def add(self,filename):
        self.queue.append(filename)

    def get(self,index):
        return self.queue[index]

    def len(self):
        return len(self.queue)

    def pop(self):
        self.queue.pop(0)