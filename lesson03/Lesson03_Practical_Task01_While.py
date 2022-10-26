#Каждый пишет сумму списка при помощи for и while

my_list = [3, 9, 42, 4, 6]
sum = 0
i = 0
while i < len(my_list):
    sum = sum + my_list[i]
    i += 1
print(sum)
