# https://www.codechef.com/LRNDSA02/problems/PSHOT

for _ in range(int(input())):
    n = int(input())
    s = input()

    remaining_a = remaining_b = n
    score_a = score_b = 0
    for i, ch in enumerate(s, 1):
        if i % 2 == 1:
            score_a += int(ch)
            remaining_a -= 1
        else:
            score_b += int(ch)
            remaining_b -= 1

        max_score_b = score_b + remaining_b
        max_score_a = score_a + remaining_a

        if score_a > max_score_b or score_b > max_score_a or i == 2 * n:
            print(i)
            break
