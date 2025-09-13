"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    pass
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    ### TODO
    pass

    this_run = 0
    max_run = 0
    for item in mylist:
        if item == key:
            this_run += 1
            max_run = max(max_run, this_run)
        else:
            this_run = 0  
    
    return max_run
            

class Result:  #package, 
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    pass

    n = len(mylist)
    if n == 0:
        return Result(0, 0, 0, True)
    if n == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    
    
    left_result  = longest_run_recursive(mylist[:len(mylist)//2], key)
    right_result = longest_run_recursive(mylist[len(mylist)//2:], key)

    
    is_entire = left_result.is_entire_range and right_result.is_entire_range

    
    left_size = left_result.left_size if not left_result.is_entire_range else (left_result.left_size + right_result.left_size)


    right_size = right_result.right_size if not right_result.is_entire_range else (right_result.right_size + left_result.right_size)

    
    longest_size = max(left_result.longest_size, right_result.longest_size, left_result.right_size + right_result.left_size)

    return Result(left_size, right_size, longest_size, is_entire)