class Solution:
    def descending_order(num):
    # Bust a move right here
        num_str = str(num)
        
        sorted_num = sorted(num_str, reverse=True)
        
        sorted_num_str = ''.join(sorted_num)
        
        sorted_num = int(sorted_num_str)
        return sorted_num
    
