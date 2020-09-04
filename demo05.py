import time
cases = [
    '" oldboy ".strip()', 
    '"   oldboy   ".strip()',
    '"--oldboy---".strip("-")',
    '"abcold-boyaaa".strip("abc")', 
]
for c in cases : 
    l = eval(c)
    print('Output of {} is : {}'.format(c, l))
    time.sleep(0.5)



