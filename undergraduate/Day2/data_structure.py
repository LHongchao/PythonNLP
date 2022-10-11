import pandas as pd

print('hellow \nworld')


def print_school_name(name):
    school_name = str(name)
    print(school_name+'is in jinan')
print_school_name(1)

a = ['shandong', 'xiamen', 'beijing','shanghai']
b = 'university'
c = 'is'
d = ['jinan','xiamen','beijing','shanghai']

for word in a:
    print(word+' '+ b+'\n')



s = str('shandong')
s1 = int(1)
s2 = float(1.5)
s3 = list(['word1','word2','word3'])

word1, word2, word3 = '着', '了' , '过'
word, pos = '跑', 'VE'
print(word1)
print(word2)
print(word3)

'''

'''
i = 3
i = [1, 2, 3, 4, 5]



print(i)
for x in i:
    print('数字%d',x)


def compare_a_b(i,j):
    if i > j:#这里是用来对比i和j的，如果i大于j的话，就执行下面的程序
        if i == 3:
            print('i = 3')
        else:
            print('i>j')
    else:
        print('j>i')

counter = [100, 200, 300, 400]
miles = 1000.0
name = 'John'

sentence = '我 喜欢 山东大学 并且 现在 在 这里 学习 。'
sentence_l = sentence.strip().split(' ')
word_len_in_sentence = [len(word) for word in sentence_l]
print(word_len_in_sentence)
total = 0
for num in word_len_in_sentence:
    total = total +num
print(total)




