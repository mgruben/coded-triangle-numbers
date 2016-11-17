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

def toInt(ch):
    return ord(ch) - 64
        
def Soltest():
    sol = Solution()
    print(sol.tri(10))
    
def readtest():
    f = open('p042_words.txt')
    for strings in f:
        # strips leading and trailing ", then splits on ","
        wordList = strings.strip("\"").split("\",\"")
    for word in wordList:
        score = 0
        for letter in word:
            score += toInt(letter)
        print(word, score)
        
if __name__=="__main__":
    readtest()
