import re
# Take-Home Assignment
# Solve the following problems.
# 1.⁠ ⁠Display Fibonacci Series upto 10 terms
def Fibonacci(i):
    if i==1:
        return 1
    elif i==2:
        return 1
    else:
        return Fibonacci(i-1)+Fibonacci(i-2)

# for i in range(1,11):
#     print(Fibonacci(i))

# 2.⁠ ⁠Display numbers at the odd indices of a list
def Odd_Number(l):
    for i in range(0,len(l)):
        if i%2!=0:
            print(l[i])
l=[2,3,4,5,6,7,8]
Odd_Number(l)


# 3.⁠ ⁠
# ⁠string = """
# I have provided this text to provide tips on creating interesting paragraphs.
# First, start with a clear topic sentence that introduces the main idea.
# Then, support the topic sentence with specific details, examples, and evidence.
# Vary the sentence length and structure to keep the reader engaged.
# Finally, end with a strong concluding sentence that summarizes the main points.
# Remember, practice makes perfect!
# """
# #Your task is to count the number of different words in this text

def Dif_word(s):
    s = re.sub(r"[^\w\s]", "", s)  
    word=s.lower().split()
    uword=set(word)
    return len(uword)

s="""
I have provided this text to provide tips on creating interesting paragraphs.
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""
print(Dif_word(s))


# 4.⁠ ⁠Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
#编写一个函数 count_vowels(word)，该函数接受一个单词作为参数，并返回该单词中元音字母的数量。
def count_vowels(word):
    count=0
    for char in word:
        if char in "aeiouAEIOU":
            count=count+1
    return count

# 5.⁠ ⁠Iterate through the following list of animals and print each one in all caps.
#animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
#遍历以下动物列表，并将每个单词以全大写形式打印出来。
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
def Big(animals):
    for animal in animals:
        print(animal.upper())#不能分开写，要直接打印出来，因为字符串是不可变的
Big(animals)


# 6.⁠ ⁠Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
def OddOrEven():
    for i in range(1,21):
        if i%2==0:
            print(str(i)+" is even")
        else:
            print(str(i)+" is Odd")

OddOrEven()
# 7.⁠ ⁠Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
def sum_of_integers(a,b):
    return a+b
print(sum_of_integers(1,2))
# Additional optional  problems are in the jupyter notebook uploaded on github