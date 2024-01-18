
# TODO Найдите количество книг, которое можно разместить на дискете

book = 100 * 50 * 25
memory_for_one_book = book * 4

memory = 1.44 * 1024 * 1024

total = round(memory / memory_for_one_book)


print("Количество книг, помещающихся на дискету:", total)
