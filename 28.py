i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                if haystack[i:i + len(needle)] == needle:
                    return(i)
            i += 1
        return -1
