'''
#รับค่ามาจำนวนหนึ่งใส่ในlist
num = []
while True:
    x = input()
    if x == 'q':
        break
    num.append(int(x))
#รับค่าตัวเลขที่ต้องการหา
ns = int(input('Enter number serch = '))
if num.index(ns):
    #แสดงผลตำแหน่งตัวเลขที่หา
    print("%d = num[%d]"%(ns,num.index(ns)))
'''
#_________________________________________________________
'''
#รับค่ามาจำนวนหนึ่งเก็บในลิส
num = []
while True:
    x = input()
    if x == 'q':
        break
    num.append(int(x))
#ทำลูปเลขเฉพาะ
ko = []
for i in num:
    k = 0
    for j in range(1,i+1):
        if i%j == 0:
            k += 1
    if k == 2:
        ko.append(i)
#แสดงจำนวนเฉพาะในลิส(ไม่ซ้ำกกัน)
io = []
for i in ko:
    y = 0
    if io == []:
        io.append(i)
        y = 1
    for j in io:
        if i == j:
            y += 1
    if y == 0:
        io.append(i)
print(io)
'''
#________________________________________
'''
num = []
while True:
    x = input()
    if x == 'q':
        break
    num.append(int(x))
##num.sort()
print(num)
y = 1
while y == 1:
    y = 0
    for i in range(0,len(num)-1):
        if num[i] > num[i+1]:
            tmp = num[i+1]
            num[i+1] = num[i]
            num[i] = tmp
            y = 1 
print(num)
'''
#_____________________________________________
'''
pro = {"soap":35,"coffee":50,"shampoo":80}
freq = {"soap":0,"coffee":0,"shampoo":0}
price = {"soap":0,"coffee":0,"shampoo":0}
#รับค่าจากแป้นพิมพ์
while True:
    du = input("product = ")
    if du == 'q':
        break
    unit = int(input("unit = "))
    if du == 'soap':
        freq['soap'] += unit
    elif du == 'coffee':
        freq['coffee'] += unit
    elif du == 'shampoo':
        freq['shampoo'] += unit
#ซื้อมากน้อย
while True:
    if freq['soap'] > freq['shampoo']:
        if freq['soap'] > freq['coffee']:
            fq3 = 'soap'
            if freq['shampoo'] > freq['coffee']:
                fq2,fq1 = 'shampoo','coffee'
            else:
                fq2,fq1 = 'coffee','shampoo'
        elif freq['soap'] < freq['coffee']:
            fq3,fq2,fq1 = 'coffee','soap','shampoo'
    elif freq['shampoo'] > freq['coffee']:
        if freq['shampoo'] > freq['soap']:
            fq3 = 'shampoo'
            if freq['coffee'] > freq['soap']:
                fq2,fq1 = 'coffee','soap'
            else:
                fq2,fq1 = 'soap','coffee'
        elif freq['shampoo'] < freq['soap']:
            fq3,fq2,fq1 = 'soap','shampoo','coffee'
    elif freq['coffee'] > freq['soap']:
        if freq['coffee'] > freq['shampoo']:
            fq3 = 'coffee'
            if freq['shampoo'] > freq['soap']:
                fq2,fq1 = 'shampoo','soap'
            else:
                fq2,fq1 = 'soap','shampoo'
        elif freq['coffee'] < freq['shampoo']:
            fq3,fq2,fq1 = 'shampoo','coffee','soap'
    break
#ราคาสินค้ามากน้อย
price['soap'] = pro['soap']*freq['soap']
price['coffee'] = pro['coffee']*freq['coffee']
price['shampoo'] = pro['shampoo']*freq['shampoo']
while True:
    if price['soap'] > price['shampoo']:
        if price['soap'] > price['coffee']:
            p3 = 'soap'
            if price['shampoo'] > price['coffee']:
                p2,p1 = 'shampoo','coffee'
            else:
                p2,p1 = 'coffee','shampoo'
        elif price['soap'] < price['coffee']:
            p3,p2,p1 = 'coffee','soap','shampoo'
    elif price['shampoo'] > price['coffee']:
        if price['shampoo'] > price['soap']:
            p3 = 'shampoo'
            if price['coffee'] > price['soap']:
                p2,p1 = 'coffee','soap'
            else:
                p2,p1 = 'soap','coffee'
        elif price['shampoo'] < price['soap']:
            p3,p2,p1 = 'soap','shampoo','coffee'
    elif price['coffee'] > price['soap']:
        if price['coffee'] > price['shampoo']:
            p3 = 'coffee'
            if price['shampoo'] > price['soap']:
                p2,p1 = 'shampoo','soap'
            else:
                p2,p1 = 'soap','shampoo'
        elif price['coffee'] < price['shampoo']:
            p3,p2,p1 = 'shampoo','coffee','soap'
    break

x = price['soap']+price['coffee']+price['shampoo']
print('Money to pay = ',x)
print('product frequent = %s %s %s'%(fq3,fq2,fq1))
print('product expensive = %s %s %s'%(p3,p2,p1))
'''
#_______________________________________________________
   # ma[0].append(du)
   # ma[1].append(unit)
#for i in range(len(ma[0])):
 #   x += pro[ma[0][i]] * ma[1][i]
  #  if pro[ma[0][i]] == 'soap':
   #     y += pro[ma[0][i]] * ma[1][i]
    #elif pro[ma[0][i]] == 'coffee':
    #    z += pro[ma[0][i]] * ma[1][i]
    #elif pro[ma[0][i]] == 'shampoo':
     #   q += pro[ma[0][i]] * ma[1][i]
#ma[1].clear()
#ma[1].append(x)
#ma[1].append(y)
#ma[1].append(z)
#ma[1].sort()
#ma[1].reverse()
#while j == 1:
#    j = 0
 #   for i in range(0,len(ma[0])-1):
  #      if ma.count(ma[0][i]) > ma.count(ma[0][i+1]):
   #         tmp = ma[0][i]
    #        ma[0][i] = ma[0][i+1]
     #       ma[0][i+1] = tmp
      #      j = 1
#while True:
 #   if 'soap' not in ma[0]:
  #      while True:
   #         if ma.count(ma[0][0]) > 1:
    #            ma[0].pop(0)
     #       else:
      #          break
       # while True:
        #    if ma.count(ma[0][1]) > 1:
         #       ma[0].pop(1)
          #  else:
           #     break
    #elif 'shampoo' not in ma[0]:
     #   while True:
      #      if ma.count(ma[0][0]) > 1:
       #         ma[0].pop(0)
        #    else:
         #       break
        #while True:
         #   if ma.count(ma[0][1]) > 1:
          #      ma[0].pop(1)
           # else:
            #    break
    #elif 'coffee' not in ma[0]:
     #   while True:
      #      if ma.count(ma[0][0]) > 1:
       #         ma[0].pop(0)
        #    else:
         #       break
        #while True:
         #   if ma.count(ma[0][1]) > 1:
          #      ma[0].pop(1)
           # else:
            #    break
    #else:
     #   while True:
      #      if ma.count(ma[0][0]) > 1:
       #         ma[0].pop(0)
        #    else:
         #       break
        #while True:
         #   if ma.count(ma[0][1]) > 1:
          #      ma[0].pop(1)
           # else:
            #    break
        #while True:
         #   if ma.count(ma[0][2]) > 1:
          #      ma[0].pop(2)
           # else:
            #    break
    #break
#print('moey use = %d'%x)
#print('produc freq = ',ma[0])
#print('produc expen = ',ma[1])
'''
ma = [1,2,1,5,3,1,1,8,5,3,3]
print(ma.count(ma[1]))
j = 1
while j == 1:
    j = 0
    for i in range(0,len(ma)-1):
        if ma.count(ma[i]) > ma.count(ma[i+1]):
            tmp = ma[i]
            ma[i] = ma[i+1]
            ma[i+1] = tmp
            j = 1
print(ma)

while True:
    if 'soa' not in ma:
        while True:
            if ma.count(ma[0]) > 1:
                ma.pop(0)
            else:
                break
        while True:
            if ma.count(ma[1]) > 1:
                ma.pop(1)
            else:
                break
    elif 'sh' not in ma:
        while True:
            if ma.count(ma[0]) > 1:
                ma.pop(0)
            else:
                break
        while True:
            if ma.count(ma[1]) > 1:
                ma.pop(1)
            else:
                break
    elif 'cof' not in ma:
        while True:
            if ma.count(ma[0]) > 1:
                ma.pop(0)
            else:
                break
        while True:
            if ma.count(ma[1]) > 1:
                ma.pop(1)
            else:
                break
    else:
        while True:
            if ma.count(ma[0]) > 1:
                ma.pop(0)
            else:
                break
        while True:
            if ma.count(ma[1]) > 1:
                ma.pop(1)
            else:
                break
        while True:
            if ma.count(ma[2]) > 1:
                ma.pop(2)
            else:
                break
    break
ma.reverse()    
print(ma)
'''      
        
        
    









