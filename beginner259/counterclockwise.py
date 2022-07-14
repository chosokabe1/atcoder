import math
s = input().split()
A = int(s[0])
B = int(s[1])
D = int(s[2])

r = math.hypot(A,B)
theta = math.atan2(B, A)
theta += D * math.acos(-1.0) / 180.0
X = math.cos(theta) * r
Y = math.sin(theta) * r
print(f"{X} {Y}")