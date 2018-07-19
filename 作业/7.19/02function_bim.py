def funcition_bin(name,height,weight):
    BIM = weight / height ** 2
    if BIM < 18.5:
        print('%s的身高是:%.2f\t体重:%d\n%s的BIM指数为:%.2f\n过瘦,请注意饮食'%(name,height,weight,name,BIM))
    elif BIM > 18.5 and BIM < 24.9:
        print('%s的身高是:%.2f\t体重:%d\n%s的BIM指数为:%.2f\n正常,请保持身材'%(name,height,weight,name,BIM))
    elif BIM >24.9 and BIM <29.9:
        print('%s的身高是:%.2f\t体重:%d\n%s的BIM指数为:%.2f\n您的体重有点过重诶'%(name,height,weight,name,BIM))
    elif BIM > 29.9:
        print('%s的身高是%.2f:\t体重:%d\n%s的BIM指数为:%.2f\n您超重了'%(name,height,weight,name,BIM))
    return
funcition_bin('路人甲',1.83,60)
print('')
funcition_bin('路人乙',1.6,50)
