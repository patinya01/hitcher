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
