#Q1
def count_start_ways(n):
    if n<0:
        return 0;
    elif n==0:
        return 1
    else:
        return count_start_ways(n-1)+count_start_ways(n-2)
#Q2
def count_k(n,k):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        totol_ways=0
        for i in range(1,k+1):
            if n-i>=0:
                totol_ways+=count_k(n-1,k)
        return totol_ways
               
#Q3
def even_weighted_loop(s):
    d=[]
    for i in range(len(s)):
        if i%2!=0|i==0:
            d.append(s[i])
    return d
    return [s[i]*i for i in s if i%2!=0]

#Q5
 def max_product(s):
     n = len(s)
     max_prod = 1

     def find_max_product_recursive(index, current_product):
         nonlocal max_prod
         if index >= n:
             max_prod = max(max_prod, current_product)
             return

        # 不选择当前元素
         find_max_product_recursive(index + 1, current_product)

        # 选择当前元素
         find_max_product_recursive(index + 2, current_product * s[index])

     find_max_product_recursive(0, 1)
     return max_prod
  


  #Q6
  