def process_arr(inp_string):
    inp_string = inp_string.split(',')
    nums = [ number for number in inp_string]
    nums.sort()
    unique_nums = set(nums)
    num_count = {}
    
    #Initializing the count dictionary.
    for number in unique_nums:
        num_count[number] = 0
    
    #Creating a dictionary with count of each number as value.
    for single_num in unique_nums:
        for num in nums:
            if single_num == num:
                num_count[single_num] += 1
            else:
                pass
    
    count_nums = list(num_count.values()) #Fetching count of all numbers in one list
    #Check for duplicate values, if any return false, else true.
    count_nums.sort()
    for i in count_nums:
        if count_nums.count(i) > 1:
            return False
        else:
            return True

if __name__ == '__main__':
    inp_string = input('Enter the array: ')
    result = process_arr(inp_string)
    print(result)