from calculate_primes import is_prime

test_numbers = {
    15193279067: True,
    23825796097: True,
    81333663659: True,
    34120744543: True,
    33212171243: True,
    46227244837: True,
    54441944917: True,
    76324851527: True,
    60670630819: True,
    23641451521: True,
    84818369101: True,
    25499053211: True,
    61869505013: True,
    25356988981: True,
    79368650903: True,

    94534313867: False,
    96506709683: False,
    51234240450: False,
    2281941006: False,
    62326083313: False,   # composite
    91850383112: False,
    33578824982: False,
    76354864722: False,
    14606523855: False,
    61564208919: False,   # composite
    20478800226: False,
    70502500896: False,
    98667643518: False,
    11305803053: False,
    91666255315: False,
}

score = []

for i in test_numbers:
    score.append(is_prime(i) == test_numbers[i])

print(score)
