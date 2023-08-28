A = [1, 2, 3, 4, 5]
B = [0, 0, 0, 0, 0]

def f(n, k): 
    global A, B
    if n >= k:
        print(B)
        return
    else:
        B[n] = A[n]
        
f(0, 5)
