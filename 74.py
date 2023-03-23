if not matrix or not matrix[0]:
            return False
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False
