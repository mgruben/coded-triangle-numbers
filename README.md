# coded-triangle-numbers 
Count the number of triangular words in a given text file.

### Triangular Words
A triangular word is a word whose letter scores sum to a triangle number.

### Triangle Numbers
The nth term of a sequence of triangle numbers is given by `n * (n + 1) / 2`  

So, the first ten triangle numbers are `1, 3, 6, 10, 15, 21, 28, 36, 45, 55`

### Letter Scores
Assume that each letter has a score based off of its position in the alphabet:
```
A = 1
B = 2
...
Y = 25
Z = 26
```
We can calculate a word score by summing the individual letter scores.
* Ex. `YAY = 25 + 1 + 25 = 51`

### Additional Data
Given the [provided](https://projecteuler.net/project/resources/p042_words.txt) text file, count how many of the words are triangular words.

### Motivation
This project was completed for [Project Euler - Problem 42](https://projecteuler.net/problem=42).

I recommend that this code should only be viewed _after_ you've completed your own implementation.  
If you're super stuck, take a break, take a walk, and it will come to you; good luck.
