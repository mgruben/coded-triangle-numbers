class Solution(object):
    def __init__(self):
        self.lookup = [1]
        self.n = 1
        
    def isTriangle(self, num):
        if num in self.lookup:
            return True
        else:
            while num > self.lookup[-1]:
                self.n += 1
                self.lookup.append(self.tri(self.n))
        if num == self.lookup[-1]:
            return True
        return False
        
    def tri(self, n):
        return int(0.5 * n * (n + 1))

def toInt(ch):
    return ord(ch) - 64
        
def Soltest():
    sol = Solution()
    for i in [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]:
        print(sol.isTriangle(i + 1))
    
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
    Soltest()
