'''
支付宝的蚂蚁森林通过日常的走步、生活缴费、线下支付、网络购票、共享单车等低碳、环保行为可以积累能量,当能量达到一定数量后,就可以种一颗真正的树。那么本实战将模拟支付宝蚂蚁森林的能量产生过程。(使用while循环) 示例效果如图： 
'''
energy = None
while energy != '0':
    print ('能量来源如下:')
    print ('生活缴费、行走捐、共享单车、线下支付、网络购票' )
    energy = input ('查询能量请输入能量来源！退出程序请输入0:')
    if energy == '生活缴费':
        print ('200g')
    elif energy == '行走捐':
        print ('300')
    elif energy == '共享单车':
        print ('350')
    elif energy == '线下支付':
        print ('380')
    elif energy == '网络购票':
        print ('500')
print ('已退出')

