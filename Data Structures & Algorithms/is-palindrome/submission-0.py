class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            # Left side par non-alphanumeric character skip karo
            if not s[left].isalnum():
                left += 1
                continue

            # Right side par non-alphanumeric character skip karo
            if not s[right].isalnum():
                right -= 1
                continue

            # Dono characters ko lowercase mein compare karo
            if s[left].lower() != s[right].lower():
                return False

            # Dono characters match hue, pointers aage badhao
            left += 1
            right -= 1

        return True