# O(n^2)T |   O(1)S
def TwoNumberSum(array, TargetSum):
    for i in range(len(array)):
        Firstnum = array[i]
        for j in range(i + 1, len(array)):
            Secondnum = array[j]
            if Firstnum + Secondnum == TargetSum:
                print(Firstnum, Secondnum)


array = [1, 2, 3, 8, 5]
TargetSum = 10
TwoNumberSum(array, TargetSum)


# O(n)T   |   O(1)S
def TwoNumberSum(array, TargetSum):
    nums = {}  # to store hashing table
    for num in array:
        potentialmatch = TargetSum - num  # y=x+sum
        if potentialmatch in nums:
            print(potentialmatch, num)
        else:
            nums[num] = True


array = [1, 2, 3, 8, 5]
TargetSum = 10
TwoNumberSum(array, TargetSum)
