import time
import random
elem = [random.randint(13, 25) for i in range(1000000)]
#print(elem)
start_time = time.time()
print(sorted(elem))
end_time = time.time()
print("время выполнения {} секунд".format(end_time - start_time))
start_time = time.time()
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
print(q(elem))
end_time = time.time()
print("время выполнения {} секунд".format(end_time - start_time))

def merge_sort(collection: list) -> list:


    def merge(left: list, right: list) -> list:

        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))

start_time = time.time()
print(merge_sort(elem))
end_time = time.time()
print("время выполнения {} секунд".format(end_time - start_time))