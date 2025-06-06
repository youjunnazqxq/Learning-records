##Mutability
'''对于append,extend,insert,remove(移除第一个出现匹配的值的),pop(索引)'''
# Q1
[1,2,3,4]
[1,2,3,4]
[1,2,3]
True
6
[-1,0,1]
6
False



# Q2
def add_this_many(x,el,s):
    count=0
    for i in s:
        if i==x:
            count+=1
    while(count>0):
        s.append(el)
        i-=1
    return None

#Q3
'c'
'S'
['6','1','a']
1
2


# Q5
def filter_iter(iterable,f):
    yield from [x for x in iterable if f]

# Q6
def is_prime(n):
    def help(i):
        if i>(n**0.5):
            return True
        elif n%i==0:
            return False
        return help(i+1)

    return help(2)

def primes_gen(n):
    while n>1:
        if is_prime(n):
            yield n
        n-=1



def prime_gen2(n):
    if n==1:
        return 
    if is_prime(n):
        yield n
    yield from prime_gen2(n-1)



# Q7
def preorder(t):
    if is_leaf:
        return [label(t)]
    first=[]
    for b in branches(t):
        first+=preorder(b)
    return [label(t)]+first

def preorder_2(t):
    yield label(t)
    for b in branches(t):
        yield from preorder(b)




#Q8





    























































    
# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])