import time
cases = [
    '123',
    '-1',
    '0.01',
    '3e5',
    '192.168.1.1',
    'abcxyz',
]
for c in cases : 
    print('Output of \'{}\'.isdigit() is :{}'.format(c, c.isdecimal()))
    time.sleep(0.5)