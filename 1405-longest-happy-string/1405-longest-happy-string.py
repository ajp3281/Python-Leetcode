class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # do one character at a time!!
        heap = []
        if a > 0:
            heap.append((-a,"a"))
        if b > 0:
            heap.append((-b,"b"))
        if c > 0:
            heap.append((-c,"c"))

        heapq.heapify(heap)
        string = ""
        while heap:
            count, char = heapq.heappop(heap)
            count *= -1

            if len(string) >= 2 and string[-1] == char and string[-2] == char:
                if not heap:
                    return string
                next_count, next_char = heapq.heappop(heap)
                string += next_char
                next_count += 1
                if next_count < 0:
                    heapq.heappush(heap,(next_count, next_char))

            string += char
            count -= 1
            if count > 0:
                heapq.heappush(heap, (count*-1, char))
        return string