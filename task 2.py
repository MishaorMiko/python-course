x=10
y=int(input('san engiz:'))
while True:
    if x==y:
        print('taptyn')
        break
    elif  x>y:
        print('seb tabpadyn x ulken')
        y = int(input('san engiz:'))
    elif x<y:
        print('seb tabpadyn x kisi')
        y = int(input('san engiz:'))
