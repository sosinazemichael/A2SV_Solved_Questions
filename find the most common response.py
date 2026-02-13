class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        count = defaultdict(int)

        for response in responses:
            for resp in set(response):
                count[resp] += 1

        max_count = max(count.values())
        most_common = min(resp for resp, cnt in count.items() if cnt == max_count)

        return most_common
