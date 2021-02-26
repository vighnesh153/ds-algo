# https://www.codechef.com/LRNDSA01/problems/ZCO14003

from collections import Counter

budgets = []
for _ in range(int(input())):
    budgets.append(int(input()))

costs = sorted(Counter(budgets).items(), reverse=True)

maximum = 0
people = 0
for cost, count in costs:
    people += count
    maximum = max(maximum, people * cost)

print(maximum)
