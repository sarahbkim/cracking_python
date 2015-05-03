import unittest
from pythonds.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for  name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()



class testPotato(unittest.TestCase):
    def test_simple(self):
        arr = ["Bill","David","Susan","Jane","Kent","Brad"]
        self.assertEquals(hotPotato(arr,7), 'Susan')

if __name__ == '__main__':
    unittest.main()