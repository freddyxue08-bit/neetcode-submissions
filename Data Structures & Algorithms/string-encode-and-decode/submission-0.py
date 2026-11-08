class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # 1. Find the "#" that ends the length number
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])        # the digits between i and the "#"

            # 2. Take exactly `length` characters after the "#"
            start = j + 1
            result.append(s[start:start + length])

            # 3. Jump to the beginning of the next length
            i = start + length
        return result
