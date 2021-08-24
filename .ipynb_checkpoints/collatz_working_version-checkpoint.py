import pandas as pd 
def get_raw_nums(n):
    nums = []
    nums.append(n)
    while n > 1:
        if n % 2 == 0 :
            n = n//2
            nums.append(n)
        else:
            n = 3*n+1
            nums.append(n)
    return nums

def get_tuples(nums):
    a = []
    for i in range(1, len(nums)):
        a.append((nums[i-1],nums[i]))
    return a 









max_size = 500
l = list(range(5000))
l1 = [l[i*max_size: (i+1)*max_size] for i in range(10)]

for item in l1:
    y = []
    for items in item:
        y.extend(get_tuples(get_raw_nums(items)))
    df = pd.DataFrame(y)
    df.columns = ['source','target'] 
    print(len(df))
    # output df to CSV - might also want to combine the dataframes into a single one if it makes sense 
    