import time
my_bill = [
    ('周一','吃饭',50),
    ('周二','打车',30),
    ('周三','购物',2313),
]
rpt_d = []
total = 0
for b in my_bill :
    total += b[2]
    rpt_d += [
        '今天{0[0]}，我去{0[1]}消费了{0[2]}元，截止今日共消费{1}元，今日消费占当前消费的{2:.2%}。'
            .format(b, total, b[2]/total)
    ]
output = '\n'.join(rpt_d)
print(output)
