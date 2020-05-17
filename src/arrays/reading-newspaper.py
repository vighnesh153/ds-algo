def solve(lines, lines_per_day):
    count = 0
    day = 1
    while count < lines:
        count += lines_per_day[day - 1]
        day += 1
        day = day if day <= 7 else day - 7
    return day - 1 if day != 1 else 7


res = solve(100, [15, 20, 20, 15, 10, 30, 45])
print(res)
