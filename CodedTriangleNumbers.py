class Solution(object):
    def __init__(self):
        self.lookup = {1: 1}
        self.n = 1
        
    def getTriangle(self, n):
        while self.n < n:
            self.n += 1
            self.lookup[n] = self.tri(n)
        return self.lookup[n]
        
    def tri(self, n):
        return int(0.5 * n * (n + 1))
        
def test():
    sol = Solution()
    print(sol.tri(10))

if __name__=="__main__":
    test()
