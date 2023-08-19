while True:
    H1, M1, H2, M2 = list(map(int,input().split()))
    if H1 == M1 == H2 == M2 == 0:
        break
    if H1 == 0:
        H1 = 24
    if H2 == 0:
        H2 = 24
    if H1 >  H2:
     H2 = H2 + 24
     aux = (H2*60+M2)-(H1*60+M1)
    elif H1 == H2 and M1 > M2:
       aux = (H2*60+M2)-(H1*60+M1)+24*60
    elif H1 == H2 and M1 == M2:
       aux = 24*60
    else:
       aux = (H2*60+M2)-(H1*60+M1)
    print(aux)