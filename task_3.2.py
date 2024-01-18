def find_common_participants(first,second, splitter =','):

    first_group = first.split(splitter)
    second_group = second.split(splitter)
    first_group_set = set(first_group)
    result = first_group_set.intersection(second_group)
    return(list(result))



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group,participants_second_group, '|')

print(sorted(result))