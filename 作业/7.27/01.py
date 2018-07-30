file = open('/home/ws/Desktop/richangzuoye/作业/7.27/01_随机内容.py','r')
while True:
    text = file.readline()
    if len(text) == 0:
        break
    if text[0] == '#':
        continue
    else:
        print(text)

file.close()
