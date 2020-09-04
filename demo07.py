import time
cases = [
    "''.join('a','b')", 
    "''.join(['a','b'])", 
    "','.join([1,2,3])", 
    "'-,'.join(['1','2','3'])", 
]
for c in cases : 
    try :
        l = eval(c)
        print('Output of {} is : {}'.format(c, l))
    except Exception as e :
        print('ERROR: {}, CAUSED BY {}'.format(str(e), c))
    finally :
        time.sleep(0.5)

