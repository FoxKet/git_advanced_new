NVIDIA_num = int(input("Введите кол-во видеокарт: "))

Cards = []
new_Cards = []
maxItem = 0

for item in range(NVIDIA_num):
    Cards.append(int(input(f'Видеокарта {item+1}: ')))
    if Cards[item] > maxItem:
        maxItem = Cards[item]

for item in range(NVIDIA_num):
    if Cards[item] != maxItem:
        new_Cards.append(Cards[item])

print('Старый список видеокарт: ', Cards,'\n','Новый список видеокарт:', new_Cards)
