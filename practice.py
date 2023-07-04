# import array as arr
# reverse a string

myStr = 'omkar'

# print(myStr[::-1])

# def revereString():
#     myStr = 'omkar how are you'
#     rStr = ''
#     # for char in myStr:
#     #     rStr = char + rStr

#     for index in range(len(myStr)):
#         rStr = myStr[index] + rStr

#     print(rStr)


# revereString()

# =========================================================== #
# =========================================================== #
# =========================================================== #

# array slice operations

myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("the array is: ", myArr)
print()
print()
print("===Using inbuilt array methods===")
# syntax
# myArr[start:end:steps]

# reverse an array
print("reversed arr: ", myArr[::-1])

# slicing or array
print("slicing from 1 to 4: ", myArr[1:4])

# negative values
print("negative number slicing: ", myArr[-2:-6:-1])

print()
print()

print("===Using custom function===")


def arrayMethods(arr, start=0, end=0, steps=1):
    finalArr = []

    def printArr():
        for i in range(start, end, steps):
            finalArr.append(arr[i])
        return finalArr

    try:
        if (end > len(arr)):
            end = len(arr)
            printArr()
            return

        if (start <= -1 and end <= -1):
            start = arr[len(arr) + start - 1]
            end = arr[len(arr) + end - 1]
            printArr()

        if (start >= 0 and end >= 0 and steps >= 0):
            printArr()

        if start == 0 and end == 0 and steps == -1:
            for i in range(len(arr)):
                lastElement = arr[len(arr)-1]
                finalArr.append(lastElement-i)

        return finalArr

    except ValueError:
        print('ValueError: slice step cannot be zero')


print("reversed array: ", arrayMethods(myArr, 0, 0, -1))
print("slicing from 1 to 4: ", arrayMethods(myArr, 1, 4))
print("negative number slicing: ", arrayMethods(myArr, -2, -6, -1))
