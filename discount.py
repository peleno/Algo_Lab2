import random


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition3(array, left, right):
    pivot = array[left]
    i = left
    leftmost_pivot_index = left
    rightmost_pivot_index = right
    while i <= rightmost_pivot_index:
        if array[i] > pivot:
            swap(array, leftmost_pivot_index, i)
            leftmost_pivot_index += 1
            i += 1
        elif array[i] == pivot:
            i += 1
        else:
            swap(array, i, rightmost_pivot_index)
            rightmost_pivot_index -= 1
    return leftmost_pivot_index, rightmost_pivot_index


def quick_select(array, left, right, n_largest):
    if left >= right:
        return
    random_pivot_index = random.randint(left, right)
    swap(array, left, random_pivot_index)
    leftmost_pivot_index, rightmost_pivot_index = partition3(array, left, right)
    if leftmost_pivot_index > n_largest - 1:
        quick_select(array, left, leftmost_pivot_index - 1, n_largest)
    elif rightmost_pivot_index < n_largest - 1:
        quick_select(array, rightmost_pivot_index + 1, right, n_largest)
    else:
        return


def count_min_sum(prices, discount):
    count_of_discounts = len(prices) // 3
    quick_select(prices, 0, len(prices) - 1, count_of_discounts)

    sum_with_discount = 0
    sum_without_discount = 0
    for i in range(count_of_discounts):
        sum_with_discount += prices[i]

    for i in range(count_of_discounts, len(prices)):
        sum_without_discount += prices[i]
    total_sum = sum_without_discount + sum_with_discount * (100 - discount) / 100
    return total_sum


if __name__ == '__main__':
    prices = input()
    prices = list(map(lambda x: int(x), prices.split()))
    discount = int(input())
    total_sum = count_min_sum(prices, discount)
    print(total_sum)