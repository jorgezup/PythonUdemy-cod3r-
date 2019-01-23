import time
for x in range(1, 11):
    if x % 2 == 0:
        continue
    time.sleep(0.2)
    print(x)

for x in range(1, 11):
    if x == 5:
        break
    print(x)