class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)
        left = 0
        s1_count = {}
        window_count = {}

        # Count characters in s1
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        # Count characters in the first window of s2
        for char in s2[:k]:
            window_count[char] = window_count.get(char, 0) + 1

        # Check the first window
        if s1_count == window_count:
            return True

        # Slide the window
        for right in range(k, len(s2)):
            # Remove the outgoing character
            window_count[s2[left]] -= 1

            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            left += 1

            # Add the incoming character
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # Compare character frequencies
            if s1_count == window_count:
                return True

        return False