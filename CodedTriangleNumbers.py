class Solution(object):
    '''
    Class for memoizing the triangular numbers.
    '''
    
    def __init__(self):
        '''
        We know at least that the first triangular number is 1.
        '''
        self.lookup = [1]
        self.n = 1
        
    def isTriangle(self, num):
        '''
        Returns True if the given 'num' is a Triangular Number,
                False otherwise.
        '''
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
        '''
        Calculates the nth triangular number according to the
        formula given on Project Euler.
        '''
        return int(0.5 * n * (n + 1))


def toInt(ch):
    '''
    Returns the "score" of the given uppercase letter.
    e.g. toInt('A') -> 1, and toInt('Z') -> 26
    '''
    return ord(ch) - 64
        
def main():
    # Build our word list
    f = open('p042_words.txt')
    for strings in f:
        # strips leading and trailing ", then splits on ","
        wordList = strings.strip("\"").split("\",\"")
    
    # Create our memo pad
    sol = Solution()
    
    # Iterate over the words and test for Triangularity
    numTriangularWords = 0
    for word in wordList:
        score = 0
        for letter in word:
            score += toInt(letter)
        if sol.isTriangle(score):
            numTriangularWords += 1
    
    # Output how many words in the given file were Triangular
    print(numTriangularWords)
        
if __name__=="__main__":
    main()
