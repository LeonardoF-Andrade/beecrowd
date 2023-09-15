import math

V, N = list(map(int, input().split()))
R = V*N
print(math.ceil(R*0.1),math.ceil(R*0.2),math.ceil(R*0.3),math.ceil(R*0.4),math.ceil(R*0.5),math.ceil(R*0.6),math.ceil(R*0.7),math.ceil(R*0.8),math.ceil(R*0.9))