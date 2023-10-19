#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        print([])
        return
    elif length == 1:
        print ([0])
        return
        
    
    fib_list = [0,1]
    while len(fib_list) < length:
        next_value = fib_list[-1] + fib_list[-2]
        fib_list.append(next_value)
    print(fib_list)
    
    

# print_fibonacci(10)
