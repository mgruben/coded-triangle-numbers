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
        
def main():
    f = open('p042_words.txt')
    for strings in f:
        # strips leading and trailing ", then splits on ","
        wordList = strings.strip("\"").split("\",\"")
    
    sol = Solution()
    
    numTriangularWords = 0
    for word in wordList:
        score = 0
        for letter in word:
            score += toInt(letter)
        if sol.isTriangle(score):
            numTriangularWords += 1
            
    print(numTriangularWords)
        
if __name__=="__main__":
    main()
