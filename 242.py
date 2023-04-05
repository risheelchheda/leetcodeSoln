if len(s) != len(t):
            return False
    
        # Create two dictionaries to store the frequency of each character in s and t
        s_freq = {}
        t_freq = {}
        
        # Loop through each character in s and t
        for i in range(len(s)):
            # Increment the frequency of the current character in the corresponding dictionary
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1
            
        # Compare the two dictionaries
        return s_freq == t_freq
