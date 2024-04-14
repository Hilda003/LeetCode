class Solution:
    def range(chars):
        start, end = chars.split('-')
        if start.islower() and end.islower():
            return ''.join(chr(i) for i in range(ord(start), ord(end) + 1))
        elif start.isupper() and end.isupper():
            return ''.join(chr(i) for i in range(ord(start), ord(end) + 1)).upper()

