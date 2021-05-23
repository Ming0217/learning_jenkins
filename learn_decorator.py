# define a decorator

def multiplier_by_two_decorator(func):
    def wrapper(*args):
        original_result = func(*args)
        modified_result = original_result*2
        return modified_result
    return wrapper

@multiplier_by_two_decorator
def compute(input):
    return(input)

if __name__=='__main__':
   f = open("mytest.txt", "w")
   f.write(str(compute(23)))
   f.close()
  # print(compute(23))


