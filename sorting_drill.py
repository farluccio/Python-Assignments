# sorting program created from scratch
#
# Created by Eric Farley in Python 2.7.13

originalList = [3,67,45,2,13,1,998]
secondList = [89, 23, 33, 45, 10, 12, 45, 45, 45]


def my_sort(sortMe):
    sortedList = []

    lengthOfSortMe = len(sortMe)
    # print lengthOfSortMe  # used for troubleshooting, can delete if needed

    sortedList.append(sortMe[(lengthOfSortMe - 1)]) # taking the last value of sortMe and initializing sortedList

    for item in range(0,(lengthOfSortMe - 1)): 
        getNum = sortMe[item]
        # print('getNum: ',getNum) # used for troubleshooting, can delete if needed
        # print('sortedList ',sortedList)  # used for troubleshooting, can delete if needed
        lengthOfSortedList = len(sortedList)

        flag = True        
        for num in range(0,lengthOfSortedList):
            if getNum <= sortedList[num]:
                sortedList.insert(num, getNum)
                flag = False
                break
        while flag:     # this adds the getNum if the above if statement doesn't fire
            sortedList.append(getNum)
            flag = False
            
    print sortedList
