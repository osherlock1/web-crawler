


class Queue:
    def __init__(self):
        self.q = []

    def push(self, link, depth):
        storage = (link, depth)
        self.q.append(storage)

    def pop(self):
        return self.q.pop()
    
    def is_empty(self) -> bool:

        if len(self.q) == 0:
            return True
        else:
            return False

    
    
    