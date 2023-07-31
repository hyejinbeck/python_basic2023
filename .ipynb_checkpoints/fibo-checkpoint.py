def fib_loop(n):
    result = [1, 1]

    for i in range(1, n):
        end1 = result[-1]
        end2 = result[len(result)-2]
        fib_num = end1 + end2

        result.append(fib_num)

    return result[-1]


def fib_rec(n):
    if n == 0 or n == 1:           # 0과 1은 어자피 1나온다. 
        return 1
    else :                         # 2부터는 아래 값으로  
        return fib_rec(n-1) + fib_rec(n-2)
    
fib_rec(10)         # fib_rec(10-1)= fib_rec(9-1) = ... 
                    # 이렇게 계~속 하나씩 작게 계산해서 호출하고 호출하고 호출