"""
Useful for counting data in dictionary
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)

print(word_counts)

print(top_three)

print(word_counts['not'])

print(word_counts['eyes'])

# Update word_counts
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

# using for loop
for word in more_words:
    word_counts[word] += 1

# or use update method
word_counts.update(more_words)

print('*'*50)
# Math operation to add, subtract counts
a = Counter(words)
b = Counter(more_words)
print(a)
print(b)
print('*'*50)
print(a + b)
