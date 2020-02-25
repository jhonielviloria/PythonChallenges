# 1352
# Implement the class ProductOfNumbers that supports two methods:
# 1. add(int num)
# Adds the number num to the back of the current list of numbers.
# 2. getProduct(int k)
# Returns the product of the last k numbers in the current list.
# You can assume that always the current list has at least k numbers.


from math import prod


class ProductOfNumbers:
    def __init__(self):
        self.lst = []

    def add(self, num: int) -> None:
        self.lst.append(num)

    def getProduct(self, k: int) -> int:
        return prod(self.lst[-k:], start=1)

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)