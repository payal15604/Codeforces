def line_breaks(t, test_cases):
    results = []
    for test in test_cases:
        n, m, words = test
        total_length = 0
        count = 0
        for word in words:
            if total_length + len(word) > m:
                break
            total_length += len(word)
            count += 1
        results.append(count)
    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]
    test_cases.append((n, m, words))

# Solve and output results
results = line_breaks(t, test_cases)
for res in results:
    print(res)
