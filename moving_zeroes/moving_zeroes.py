'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    positive = []
    negative = []
    zero = []

    for i in range(len(arr)):
        if arr[i] > 0:
            positive.append(arr[i])
        elif arr[i] < 0:
            negative.append(arr[i])
        else:
            zero.append(arr[i])

    return positive + negative + zero


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
