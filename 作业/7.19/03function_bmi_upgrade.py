def function_bim_upgrade(name,height,weight):
    BIM = weight / height ** 2
    if BIM < 18.5:
        ws_name = '过轻'
    elif BIM > 18.5 and BIM < 24.9:
        ws_name = '正常'
    elif BIM >24.9 and BIM <29.9:
        ws_name = '超重'
    elif BIM > 29.9:
        ws_name = '特重'
    print('=======================%s========================'%name)
    print('身高是%.2f米\t\t体重:%.2fkg'%(height,weight))
    print('您的的BIM是:%.2f,%s'%(BIM,ws_name))
    print('')
l = [{'name':'绮梦','height':1.7,'weight':65},{'name':'零语','height':1.78,'weight':50},{'name':'黛兰','height':1.72,'weight':66},{'name':'紫轩','height':1.8,'weight':75},{'name':'冷伊一','height':1.75,'weight':70}]
c = {}
for c in l:
    function_bim_upgrade(c['name'],c['height'],c['weight'])
    
