def longest_consecutive_ones(n):
   
    max_count = 0  
    current_count = 0  
    
    while n > 0:
       
        if (n & 1) == 1:
           
            current_count += 1
        else:
         
            max_count = max(max_count, current_count)
            current_count = 0
        
      
        n = n >> 1
    
   
    max_count = max(max_count, current_count)
    
    return max_count


n = int(input("Enter a number:"))


result = longest_consecutive_ones(n)


print(f"The longest consecutive 1's in the binary representation of {n} is {result}.")
