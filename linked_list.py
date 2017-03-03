class LinkedNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = LinkedNode(data[0])
        p = self.head
        for i in data[1:]:
            node = LinkedNode(i)
            p.next = node
            p = p.next

    def search(self, key):
        p = self.head
        result = False
        while p != None:
            if (p.key == key):
                result = True
            p = p.next
        return result

    def insert(self, key, position):
        p = self.head
        index = 0
        while p != None:
            if position == index:
                node = LinkedNode(key, p.next)
                p.next = node
                return True
            index += 1
            p = p.next
        return False

    def delete(self, key):
        p = self.head
        q = self.head
        if p.key == key:
            self.head = p.next
            return
        while p != None:
            if p.key == key:
                q.next = p.next
            q = p
            p = p.next

    def reverse(self):
        p = self.head
        while p.next != None:
            q = p.next
            p.next = q.next
            q.next = self.head
            self.head = q

    def getLength(self):
        p = self.head
        length = 0
        while p != None:
            length += 1
            p = p.next
        return length

    def printAll(self):
        p = self.head
        while p != None:
            print(p.key)
            p = p.next

def main():
    linkedList = LinkedList()
    linkedList.initList([1, 2, 3, 4, 5])
    linkedList.printAll()
    print(linkedList.search(1))

    print('---------')
    linkedList.insert(key=6, position=linkedList.getLength()-1)
    linkedList.printAll()

    print('---------')
    linkedList.delete(key=6)
    linkedList.printAll()
    print('---------')
    linkedList.reverse()
    linkedList.printAll()

if __name__ == '__main__':
    main()
