def memoize(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            print(f'Fetching from cache for {n}')
            return cache[n]
        
        print(f'Calculating new result for {n}')
        result = func(n)
        cache[n] = result
        return result
    
    return wrapper

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print('fibonacci(10) = ', fibonacci(10))
    