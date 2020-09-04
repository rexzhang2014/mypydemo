import time
cases = [
    "'{0},{2},{1}'.format('a','b','c')", 
    "'{},{},{}'.format('a','b','c')", 
    "'{0[0]},{0[2]},{0[1]}'.format(['a','b','c'])", 
    "'{:.2f},{:0>5d},{:.2%}'.format(3.14159,7,0.1234)", 
    "'{0},{},{}'.format('a','b','c')", 
]
for c in cases : 
    try :
        l = eval(c)
        print('Output of {} is : {}'.format(c, l))
        time.sleep(0.5)
    except Exception as e :
        print('ERROR: {}, CAUSED BY {}'.format(str(e), c))




