import time
cases = [
    "[1,2]+[3,4]", 
    "[1,2]+['a','b']", 
    "(1,2)+(3,4)", 
    "[a+b for a,b in zip([1,2],[3,4])]", 
]
for c in cases : 
    try :
        l = eval(c)
        print('Output of {} is : {}'.format(c, l))
    except Exception as e :
        print('ERROR: {}, CAUSED BY {}'.format(str(e), c))
    finally :
        time.sleep(0.5)

