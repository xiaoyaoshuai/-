file = open('/home/ws/Desktop/richangzuoye/作业/7.27/2数字.py','r')
while True:
    text = file.readline() 
    text1 = list(text)
    text1.sort()
    if not text:
        break
    print(text1[1:])
file.close()
