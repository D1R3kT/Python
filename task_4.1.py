# TODO решите задачу
import json
with open('input.json', 'r') as file:
    data = json.load(file)


def task() -> float:
    result = 0
    for d in data:
        result += d["score"] * d["weight"]
    return round(result, 3)



print(task())

