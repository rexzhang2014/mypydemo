import time
cases = [
    '"oldboy".center(8,"-")', 
    '"oldboy".center(7,"-")',
    '"oldboy".center(5,"-")',
    '"oldboy".center(len("oldboy")+2,"\'")', 
]
for c in cases : 
    l = eval(c)
    print('Output of {} is : {}'.format(c, l))
    time.sleep(0.5)



