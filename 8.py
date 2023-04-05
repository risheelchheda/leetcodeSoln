# Remove leading whitespaces
        str = str.lstrip()
        # Check if the string is empty
        if not str:
            return 0
        # Check if the first character is a sign
        is_negative = False
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            is_negative = True
            str = str[1:]
        # Remove leading zeros
        str = str.lstrip('0')
        # Check if the string contains only digits
        if not str or not str[0].isdigit():
            return 0
        # Find the first non-digit character
        for i in range(len(str)):
            if not str[i].isdigit():
                str = str[:i]
                break
        # Check if the converted integer is within the range of 32-bit signed integer
        if str:
            result = int(str)
            if is_negative:
                result = -result
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1
            return result
        return 0
