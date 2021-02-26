# https://www.codechef.com/LRNDSA01/problems/LADDU

for _ in range(int(input())):
    n, origin = input().split()
    n = int(n)

    laddus = 0
    for _ in range(n):
        activity = input().split()
        if activity[0] == "CONTEST_WON":
            rank = int(activity[1])
            bonus = (20 - rank) if rank <= 20 else 0
            laddus += 300 + bonus
        elif activity[0] == "TOP_CONTRIBUTOR":
            laddus += 300
        elif activity[0] == "BUG_FOUND":
            severity = int(activity[1])
            laddus += severity
        else:  # CONTEST_HOSTED
            laddus += 50

    print(laddus // (200 if origin == "INDIAN" else 400))
