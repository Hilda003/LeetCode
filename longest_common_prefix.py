class Solution:
    def longestCommonPrefix(strs):

        # varible untuk menyimpan hasil awalan & jika panjang array 0, return str

        prefix = ""

        if len(strs) == 0:
            return prefix
        
        # Inisialisasi awalan dengan string pertama dalam array

        prefix = strs[0]

        # Loop utk karakter dlm str pertama

        for i in range(len(prefix)):
            for string in strs[1:]:
                if i >= len(string) or prefix[i] != string [i]:
                    return prefix[:i]

        return prefix
    strs1 = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs1))

    strs2 = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs2))


