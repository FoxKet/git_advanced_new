orders_count = int(input('Введите колличество заказов: '))

database = dict()

for i_order in range(orders_count):
    customer, pizz_name, count = input('{} заказ: '.format(i_order+1)).split()

    count=int(count)

    if customer not in database:
        database[customer]  = {pizz_name: count}
    else:
        if pizz_name in database[customer]:
            database[customer][pizz_name] +=count
        else:
            database[customer][pizz_name] = count

for customer in sorted(database.keys()):
    print('{}:'.format(customer))
    for pizz_name in sorted(database[customer].keys()):
        print('     {}: {}'.format(pizz_name, database[customer][pizz_name]))