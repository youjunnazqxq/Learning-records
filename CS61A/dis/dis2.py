#Q6
def curry(func):
    def FUNC(x):
        def B(y):
            return func(x,y)
        return B
    return FUNC

#Q7
def f1():
    return 3
def f2():
    return lambda :3
def f3():
    return lambda : lambda x:x
def f4():
    return lambda:lambda:lambda x:lambda :x

#Q8
def lambda_curry2(func):
    return lambda x:lambda y:func(x,y)

#Q9
def match_k_alt(k):
    def check(x):
        while x //10**k:
            if(x%10)!=(x//10**k)%10:
                return False
        return True
    return check
