def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    passes = 0
    
    while swapped:
        swapped = False
        passes += 1
        
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1
    
    return arr, passes


def cocktail_sort_with_steps(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    step = 1
    
    print(f"Initial array: {arr}")
    print("-" * 50)
    
    while swapped:
        swapped = False
        
        print(f"Step {step} - Forward pass (index {start} to {end}):")
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(f"  Swapped {arr[i+1]} and {arr[i]}: {arr}")
        if not swapped:
            break
        
        swapped = False
        end -= 1
        print(f"Step {step} - Backward pass (index {end} to {start}):")
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(f"  Swapped {arr[i+1]} and {arr[i]}: {arr}")
        
        start += 1
        step += 1
    
    print("-" * 50)
    print(f"Sorted array: {arr}")
    return arr


if __name__ == "__main__":
    print("=" * 50)
    print("Cocktail Sort Algorithm Demo")
    print("=" * 50)
    
    test1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nTest Case 1 - Random: {test1}")
    sorted_arr, passes = cocktail_sort(test1.copy())
    print(f"Sorted: {sorted_arr}")
    print(f"Passes: {passes}")
    
    test2 = [1, 2, 3, 4, 5]
    print(f"\nTest Case 2 - Already sorted: {test2}")
    sorted_arr, passes = cocktail_sort(test2.copy())
    print(f"Sorted: {sorted_arr}")
    print(f"Passes: {passes}")
    
    test3 = [5, 4, 3, 2, 1]
    print(f"\nTest Case 3 - Reverse sorted: {test3}")
    sorted_arr, passes = cocktail_sort(test3.copy())
    print(f"Sorted: {sorted_arr}")
    print(f"Passes: {passes}")
    
    print("\n" + "=" * 50)
    print("Cocktail Sort - Step by Step")
    print("=" * 50)
    test4 = [6, 4, 3, 8, 1, 5]
    cocktail_sort_with_steps(test4)
