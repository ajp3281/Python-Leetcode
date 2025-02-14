class ProductOfNumbers:
    # keep running sum?
    # how can we get product in less than o(n)?
    # we can't add to the beginning..
    # prefix arr?
    # how to handle 0s?
    # how do we handle multiple 0s..
    def __init__(self):
        self.res = 1
        self.arr = [1]
        self.zeroes = set()

    def add(self, num: int) -> None:
        if num == 0:
            self.arr.append(1)
            self.zeroes.add(len(self.arr))
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        res = self.arr[-1] // self.arr[len(self.arr) - k - 1]
        for zeroes in self.zeroes:
            if (len(self.arr) - k) < zeroes < len(self.arr):
                return 0
        return res        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)