def find_max():
    try:
        x = int(input())
    except EOFError:
        return float('-inf')
    
    if x == 0:
        return float('-inf')
    
    max_rest = find_max()
    
    # Сравниваем с учетом того, что max_rest может быть -inf
    if max_rest == float('-inf'):
        return x
    return x if x > max_rest else max_rest

if __name__ == "__main__":
    print("Ответ", find_max())