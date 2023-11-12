# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, sep=','):
    participants1 = group1.split(sep)
    participants2 = group2.split(sep)

    intersection_set = set(participants1).intersection(participants2)
    common = list(intersection_set)
    common.sort()

    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)