# from time import sleep
# from threading import *

# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(0.8)

# class hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("hi")
#             sleep(0.8)

# t1=hello()
# t2=hi()


# t1.start()
# sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# print("bye")

# import os
# print(os.cpu_count())

# import sys
# from array import array

# nums = array("i", [1,2,3,4])
# print(sys.getsizeof(nums) ,"bytes")


from array import array

nums = array("i", [1,2,3,4])

print(nums.itemsize)        # bytes per element
print(len(nums))            # number of elements
print(nums.itemsize * len(nums))
import sys
print(sys.getsizeof(nums))