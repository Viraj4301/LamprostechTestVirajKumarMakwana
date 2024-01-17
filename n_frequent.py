import heapq
from collections import Counter

def top_k_frequent_elements(nums, k):
    # Use Counter to count the occurrences of each element
    counter = Counter(nums)
    
    heap = []
    
    for num, freq in counter.items():
        heapq.heappush(heap, (freq, num))
        

        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract the k most frequent elements from the heap
    result = [item[1] for item in heap]
    

    result.reverse()
    
    return result


nums = [5, 2, 5, 3, 5, 3, 1]
k = 2
result = top_k_frequent_elements(nums, k)
print(result)
