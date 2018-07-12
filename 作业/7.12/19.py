print ('演值大比拼')
hight = int(input ('请输入身高'))
money = int(input ('请输入身价'))
face = int(input ('请输入颜值'))
if hight > 180 and money > 1000000 and face > 99:
    print ('高富帅')
elif money >1000000 and face >99:
    print ('富帅')
elif face > 99:
    print ('帅')
elif hight < 160 and money <100 and face <60:
    print ('矮穷矬')
