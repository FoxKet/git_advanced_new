films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Моменто', 'Отступники', 'Деревня']

my_list = []

count = int(input('Сколько фильмов хотите добавить? '))

for _ in range(count):
    movie = input('Введите название фильма: ')

    if movie in films:
        my_list.append(movie)
    else:
        print(f'Ошибка: фильма {movie} у нас нет')

print(f'\n Ваш список фильмов: {my_list}')

