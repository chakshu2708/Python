from collections import defaultdict, Counter
str1 = 'chakshu'
my_dic = {}
for letter in str1:
    my_dic[letter] = my_dic.get(letter, 0) + 1
print(my_dic)