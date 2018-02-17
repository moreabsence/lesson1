def get_answers(question, answers):
    return answers.get(question)

answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
quesiton = input()

answer=get_answers(quesiton, answers)
print(answer)
