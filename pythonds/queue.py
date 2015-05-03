'''

* Queue() creates a new empty queue -- has no params
* enqueue(item) adds a new item to the rear of the queue
* dequeue() removes front item from queue
* isEmpty() tests to see if queue is empty
* size() returns # of items in the queue 

'''
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        mystr = ''
        for i in self.items:
            mystr += str(i) + ','
        return mystr

        

# q = Queue()
# for i in range(5):
#     q.enqueue(i)
# print q