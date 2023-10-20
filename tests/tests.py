#MASHQLAR

#1
def max_numb(x,y,z):
    return max(x, y, z)

# print(max_numb(4, 33, 109))

#2
def title_letter(words):
    new_words = []
    for word in words:
        word = word.title()
        new_words.append(word)
    return new_words

# print(title_letter(['hello', 'hi', 'goodbye']))

#3
def even_nums(nums):
    evenNumbers = []
    for num in nums:
        if num%2 == 0:
            evenNumbers.append(num)
    return evenNumbers

# print(even_nums([1,2,3,7,10,15,20]))