v1 = version1.split('.')
    v2 = version2.split('.')
    # Get the maximum length between the two lists
    n = max(len(v1), len(v2))
    # Iterate over the revisions of both lists
    for i in range(n):
        # Convert each revision to an integer if it exists, otherwise use 0
        r1 = int(v1[i]) if i < len(v1) else 0
        r2 = int(v2[i]) if i < len(v2) else 0
        # Compare revisions and return result if different
        if r1 < r2:
            return -1
        elif r1 > r2:
            return 1
    # Return 0 if all revisions are equal
    return 0
