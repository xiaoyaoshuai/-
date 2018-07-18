'''

    存在字符串 "I,love,python",取出love并输出
    存在字符串 "aabbccddee"，将dd替换为ff
    存在字符串 "ab2b3n5nn2n67mm4n2" 完成以下功能:
        统计字符串中字母n出现的次数并输出
        统计每个字符出现的次数,使用字典输出，例如 {'a':1,'b':2}....

'''
s='I,love,python'
s1='aabbccddee'
s2='ab2b3n5nn2n67mm4n2'
print(s[2:6])
print(s1.replace('d','f'))
print(s2.count('n'))
a = {}
for i in s2:
    if i in a.keys():
        a[i] += 1
    else:
        a[i] = 1
print(a)
