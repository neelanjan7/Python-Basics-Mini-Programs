nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 4:
        print('Found!')
        break
    print(num)

for num in nums:
    for letter in 'ab':
        print (nums, letter )

x = 0

while x < 10:
    if x == 8:
        break
    print (x)
    x += 1

