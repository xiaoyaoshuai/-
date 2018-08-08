for ji in range(0,31):
    if 2*ji + (30 - ji)*4 == 90:
        print(ji,(30-ji))
print('='*30)
tu = 0
while tu <= 30:
    if 2*(30-tu)+4*tu == 90:
        print(tu,(30-tu))
    tu += 1
