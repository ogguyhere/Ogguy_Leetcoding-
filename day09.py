# Leetcode no 1472 : Design Browser History 

class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.homepage = homepage
        self.historyforward = []
        self.historybackward = []
        

    def visit(self, url: str) -> None:
        self.historybackward.append(self.homepage)
        self.homepage = url
        self.historyforward.clear()
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.historybackward:
            self.historyforward.append(self.homepage)
            self.homepage = self.historybackward.pop()
            steps -=1
            
        return self.homepage

    def forward(self, steps: int) -> str:       
        while steps > 0 and self.historyforward:
            self.historybackward.append(self.homepage)
            self.homepage = self.historyforward.pop()
            steps -=1
        return self.homepage
        
obj = BrowserHistory("khadijah")

obj.visit("lol")
obj.visit("lol2")
obj.visit("lol3")

obj.forward(3)



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)