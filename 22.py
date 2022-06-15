def countString(ch,s):
    if(len(s)==0):
        return 0
    count = 0

    if (s[0]==ch):
        count+=1

    count += countString(ch,s[1:])
    return count

str = "Chakshu"
c = 'h'
print(countString(c, str))