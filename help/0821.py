def sortNums(nums,n):
    temp = []
    curr = 1
    for i in range(len(nums)):
        if i+1 >=n and curr<=n:
            temp.append(nums[i])
            curr+=1
        


if __name__ == '__main__':
    print(1)
