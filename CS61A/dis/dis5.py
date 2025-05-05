def tree(label, branches=[]):
 return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)


#Q2
def height(t):
    if is_leaf:
        return 0
    Most_height=0;
    for b in branches(t):
        Most_height=max(height(b),Most_height)
    return Most_height+1

#Q3
def max_path_sum(t):
    if is_leaf:
        return label(t)
    sum=0
    for b in branches(t):
        sum=max(max_path_sum(b),sum)
    return label(t)+sum
#Q4
def find_path(t,x):
    if label(t)==x:
        return [label(t)]
    for b in branches(t):
        path=find_path(b)
        if path:
            return label(t)+path
    return None
#Q5
def sum_tree(t):
    if is_leaf(t):
        return label(t)
    sum=label(t)
    for b in branches(t):
        sum+=sum_tree(b)
    return sum+label(t)
# return label(t)+sum([sum_tree(b) for b in branches(t)])
    
def balanced(t):
    for b in branches(t):
        if sum_tree(branches(t)[0])!=sum_tree(b)or not balanced(b):
            return False
    return True




#Q6
def sprout_leaves(t,leaves):
    if is_leaf(t):
        return tree(label(t),list[leaves])
    for b in branches(t):
        sprout_leaves(b,leaves)


#Q7
def hailstone_tree(n,h):
    if h==0:
        return tree(n)
    branches=[hailstone_tree(n*2,h-1)]
    if (n-1)%3==0 and ((n-1)//3)%2==1 and (n-1)//3>1:
        brancher+=[hailstone_tree((n-1)//3,h-1)]
    return tree(n,branches)