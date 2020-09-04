import time
cases = [
    'range(10)', # 0-9
    'range(1,10)', # 1-10
    'range(1,10,2)', # 1,3,5,7,9
    'range(10,0,-1)', # 10-1
]
for c in cases : 
    l = [i for i in eval(c)]
    print('Output of {} is : {}'.format(c, l))
    time.sleep(0.5)



