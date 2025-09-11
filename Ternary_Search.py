def ternary_search(arr, target):
    low, high = 0, len(arr) - 1

    step = 1
    while low <= high:
        # calculate two mids
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        # print the current step for dry run
        print(f"Step {step}: Range = [{low}..{high}], mid1={mid1} ({arr[mid1]}), mid2={mid2} ({arr[mid2]})")

        # check conditions
        if arr[mid1] == target:
            print(f"--> Found {target} at index {mid1}")
            return mid1
        if arr[mid2] == target:
            print(f"--> Found {target} at index {mid2}")
            return mid2

        if target < arr[mid1]:
            high = mid1 - 1
            print(f"--> Target < arr[mid1], new range = [{low}..{high}]")
        elif target > arr[mid2]:
            low = mid2 + 1
            print(f"--> Target > arr[mid2], new range = [{low}..{high}]")
        else:
            low = mid1 + 1
            high = mid2 - 1
            print(f"--> Target between arr[mid1] and arr[mid2], new range = [{low}..{high}]")

        step += 1

    print("--> Target not found")
    return -1


# Example usage
arr = [2, 4, 7, 10, 15, 18, 21, 30, 40]
target = 15
ternary_search(arr, target)
