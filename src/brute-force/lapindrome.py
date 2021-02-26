# https://www.codechef.com/LRNDSA01/problems/LAPIN

for _ in range(int(input())):
    s = input()
    first = sorted(s[0:len(s) // 2 + (1 if len(s) % 2 == 1 else 0)])
    second = sorted(s[len(s) // 2:])

    print("YES" if first == second else "NO")
