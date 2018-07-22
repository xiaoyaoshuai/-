a = {1:'0分钟',2:'50分钟',3:'100分钟',4:'300分钟',5:'不限量'}
b = {1:'0M',2:'500M',3:'1G',4:'5G',5:'不限量'}
c = {1:'0条',2:'50条',3:'100条'}
print('定制自己的手机套餐:')
print('A.请设置通话时长:')
for z,x in a.items():
    print(z,x)
z = int(input('输入选择的通话时间编号:'))
print('B.请设置流量：')
for n,m in b.items():
    print(n,m)
n = int(input('输入选择的流量编号:'))
print('C.请设置短信条数:')
for t,u in c.items():
    print(t,u)
t = int(input('请输入选择的短信编号:'))
print('您的手机套餐定制成功：免费通话时长为%s/月,流量为%s/月,短信条数%s/月'%(a[z],b[n],c[t]))
