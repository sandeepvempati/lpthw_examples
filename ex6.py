n = [[1,2,3],[4,5,6,7,8,9]]

def flatten(lists):
    results = []
    for item in lists:
        for x in range(len(item)):
            results.append(item[x])
    return results
print flatten(n)
