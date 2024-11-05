# Devon Taylor
# DS
# U3L3
# 10/30/24

def merge_sort(num_list):
  if len(num_list) == 1:
    return num_list
  half = int(len(num_list)/2)

  left = num_list[0:half]
  right = num_list[half:]
  left = merge_sort(left)
  right = merge_sort(right)

  sortedList = []
  while left and right:
    if left[0] < right[0]:
      sortedList.append(left[0])
      left.pop(0)
    else:
      sortedList.append(right[0])
      right.pop(0)
  sortedList.extend(left)
  sortedList.extend(right)
  return sortedList


def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()