hight = 1.75
weight = 85.0
BIM = float(weight)/float(hight)**2
if BIM <= 18.5:
    print ('过轻')
elif BIM >18.5 and BIM <25:
    print ('正常')
elif BIM>=25 and BIM <28:
    print ('过重')
elif BIM>=28 and BIM <32:
    print ('肥胖')
elif BIM>=32:
    print('严重肥胖')

