import time

def find_change(results, current_decomposition, n, denominations):
    """Find changes
       
       Arguments
       results               -- accumulate result in an array. Each item is also an array
       current_decomposition -- decomposition of n in denominations
       n                     -- number to decompose. Does not change
       denominations         -- array of denominations to be used for decomposition
    """
    
   # Guard conditions to stop the recursion
    if sum(current_decomposition) == n: 
        results.append(list(current_decomposition))
        return
    elif sum(current_decomposition) > n: 
        return

    # We first iterate through the denominations
    # then recursively call the function to continue
    # to find the remaining decomposition in denomination of n
    for denomination in denominations:
        my_current_decomposition = list(current_decomposition)
        my_current_decomposition.append(denomination)
        find_change(results, my_current_decomposition, n, denominations) 

    return

def main():

    # Test 1 #############################################
    expected_results =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    test(n=10,denominations=[1], expected_results=expected_results) 

    # Test 2 #############################################
    expected_results = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                        [1, 1, 8], 
                        [1, 8, 1], 
                        [8, 1, 1]]
    test(n=10,denominations=[1, 8], expected_results=expected_results) 

    # Test 3 #############################################
    expected_results =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                       [1, 1, 1, 7], 
                       [1, 1, 7, 1], 
                       [1, 1, 8], 
                       [1, 7, 1, 1], 
                       [1, 8, 1], 
                       [7, 1, 1, 1], 
                       [8, 1, 1]]
    test(n=10,denominations=[1, 7, 8], expected_results=expected_results) 

    # Test 3 #############################################
    expected_results =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                       [1, 1, 1, 1, 1, 1, 1, 3], 
                       [1, 1, 1, 1, 1, 1, 3, 1], 
                       [1, 1, 1, 1, 1, 3, 1, 1], 
                       [1, 1, 1, 1, 1, 5], 
                       [1, 1, 1, 1, 3, 1, 1, 1], 
                       [1, 1, 1, 1, 3, 3], 
                       [1, 1, 1, 1, 5, 1], 
                       [1, 1, 1, 3, 1, 1, 1, 1], 
                       [1, 1, 1, 3, 1, 3], 
                       [1, 1, 1, 3, 3, 1], 
                       [1, 1, 1, 5, 1, 1], 
                       [1, 1, 3, 1, 1, 1, 1, 1], 
                       [1, 1, 3, 1, 1, 3], 
                       [1, 1, 3, 1, 3, 1], 
                       [1, 1, 3, 3, 1, 1], 
                       [1, 1, 3, 5], 
                       [1, 1, 5, 1, 1, 1], 
                       [1, 1, 5, 3], 
                       [1, 3, 1, 1, 1, 1, 1, 1], 
                       [1, 3, 1, 1, 1, 3], 
                       [1, 3, 1, 1, 3, 1], 
                       [1, 3, 1, 3, 1, 1], 
                       [1, 3, 1, 5], 
                       [1, 3, 3, 1, 1, 1], 
                       [1, 3, 3, 3], 
                       [1, 3, 5, 1], 
                       [1, 5, 1, 1, 1, 1], 
                       [1, 5, 1, 3], 
                       [1, 5, 3, 1], 
                       [3, 1, 1, 1, 1, 1, 1, 1], 
                       [3, 1, 1, 1, 1, 3], 
                       [3, 1, 1, 1, 3, 1], 
                       [3, 1, 1, 3, 1, 1], 
                       [3, 1, 1, 5], 
                       [3, 1, 3, 1, 1, 1], 
                       [3, 1, 3, 3], 
                       [3, 1, 5, 1], 
                       [3, 3, 1, 1, 1, 1], 
                       [3, 3, 1, 3], 
                       [3, 3, 3, 1], 
                       [3, 5, 1, 1], 
                       [5, 1, 1, 1, 1, 1], 
                       [5, 1, 1, 3], 
                       [5, 1, 3, 1], 
                       [5, 3, 1, 1], 
                       [5, 5]]
    test(n=10,denominations=[1, 3, 5], expected_results=expected_results) 

def test(n, denominations, expected_results):
    print("Testing `find_change()` for n: {}, denominations: {}".format(n, denominations))
    results = []
    current_decomposition = []
    start = time.time()
    find_change(results, current_decomposition, n, denominations)
    end = time.time()
    print("Time elapsed: {}".format(end - start))
    print("Results: \n{}\n".format(results))
    assert (results == expected_results)

main()
