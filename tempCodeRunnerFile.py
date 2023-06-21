def number_of_occurance(array):
    count = {}

    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] =1
        
        
    sorted_dict = dict(sorted(count.items(), key=lambda x: -x[1]))

    for key,value in sorted_dict.items():
        return sorted_dict
    
    


if __name__ == '__main__':
    arr = list(map(int,input().split()))
    result = number_of_occurance(arr)
    for key,value in result.items():
        print(key,value)