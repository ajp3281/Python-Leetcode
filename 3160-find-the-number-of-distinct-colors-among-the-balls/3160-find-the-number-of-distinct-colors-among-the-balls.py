class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        colored = {}
        ball_to_color = {}

        res = []
        components = 0
        for query in queries:
            ball, color = query

            if color not in colored or colored[color] == 0:
                components += 1
            colored[color] = colored.get(color, 0) + 1

            if ball in ball_to_color:
                prev_color = ball_to_color[ball]
                colored[prev_color] -= 1

                if colored[prev_color] == 0:
                    components -= 1
                    
            ball_to_color[ball] = color

            res.append(components)


        return res


        