import math
N = int(input())
rings = list(map(int, input().split()))

for i in rings[1:]:
    _gcd = math.gcd(rings[0], i)
    print(f'{rings[0]//_gcd}/{i//_gcd}')
