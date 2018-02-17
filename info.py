user_info={'first_name': None,'last_name': None}
user_info['first_name']=input("Введите ваше имя")
user_info['last_name']=input("Введите вашу фамилию")
print(user_info.get('first_name'),user_info.get('last_name'))
