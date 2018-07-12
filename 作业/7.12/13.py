print ("为了您和他人的安全,严禁酒后驾车!")
m = input ('请输入每100毫升血液的酒精含量:')
if int(m)>10:
    print ('开始进行检测')
    if int(m) <= 20:
        print ('您还不构成酒后驾车行为,可以开车，但要注意安全')
    elif int(m)>20 and int(m)<80:
        print ('您属于酒后驾驶,请不要开车')
    elif int(m)>= 80:
        print ('您已经是醉酒驾驶,开车就是找死')
else:
    print ('你没喝酒,再见') 
