class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class BrowserHistory(object):

    def __init__(self, homepage):
        self.current=ListNode(homepage)
    
    def visit(self, url):

        node=ListNode(url)
        self.current.next=None
        node.prev=self.current
        self.current.next=node
        self.current=node

    def back(self, steps):
        while steps>0 and self.current.prev:
            self.current=self.current.prev
            steps-=1
        return self.current.val
        

    def forward(self, steps):
        while steps>0 and self.current.next:
            self.current=self.current.next
            steps-=1
        return self.current.val
        
