'''
在终端输入3组数据,分别为年龄（age）,专业(subject),是否重点大学(college) 录取资格:(满足其中一个条件即可录取)

    电子信息工程专业且年龄大于25岁
    电子信息工程专业且为重点大学
    年龄小于28岁且为计算机专业

否则输出:抱歉,您未达到面试要求
'''
age =int(input ('请输入年龄:'))
subject = input('请输入专业:')
college = input ('请输入您是否属于重点大学:')
if age >= 25 and subject == '电子信息工程专业':
    print ('您可以进行面试')
elif subject == '电子信息工程专业' and college == '是':
    print ('您可以进行面试')
elif age <= 28 and subject == '计算机专业':
    print ('您可以进行面试')
else:
    print ('您未达到面试要求')
