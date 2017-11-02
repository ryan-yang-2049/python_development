#!/usr/bin/env python
#coding:utf-8
'''
冒泡排序
l = [101, 97, 41, 94, 89, 81, 74, 61, 57, 91]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)

快速排序:
快速排序的思路是采用分治法将一个list分成两个子列表,它的步骤是:
在列表中选择一个元素作为”基准”(pivot) 所有小于”基准”的元素都移到基准的左边,所有大于”基准”的元素移到基准的右边.
对基准左边和右边的两个子集,重复第一步和第二步,直到子集中的元素只剩下一个元素为止 参考实现:
#!/usr/bin/env python
# Written by Magnus Lie Hetland
"Everybody's favourite sorting algorithm... :)"
def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break

            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.

            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break

            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                break                          # ...and start searching from the bottom.

    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point

def quicksort(list, start, end):
    if start < end:                            # If there are two or more elements...
        split = partition(list, start, end)    # ... partition the sublist...
        quicksort(list, start, split-1)        # ... and sort both halves.
        quicksort(list, split+1, end)
    else:
        return


选择排序:

选择排序每次从列表中查找出最小的元素,存放到已经是有序的列表中,再从剩余未排序的列表中查找最小的元素放入已排序好的列表的最后,
依次类推直到所有元素排序完毕.
def selection_sort(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1, len(l)):
            if l[min]>l[j]:
                min = j
        if l[i]!=l[min]:
            l[i],l[min] = l[min],l[i]
https://foofish.net/sort-algorithm-compare.html
'''








