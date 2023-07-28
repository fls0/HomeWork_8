from datetime import datetime, timedelta, date

users = [
    {'Andrii': '31-07-1995'},
    {'Petro': '1-08-1989'},
    {'Viktoria': '2-08-1996'},
    {'Anastasia': '29-07-1997'},
    {'Vitalii': '3-08-1999'},
    {'Polina': '4-08-1998'},
    {'Serhii': '3-08-1998'}
]

weekdays_name = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: []
}

weekdays_days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
    7: 'Next monday'
}


def get_birthday_per_week(users: list) -> list:
    new_users_dict = {}
    d_now = datetime.now()
    for i in users:  # Итерируемся по списку словарей, меняем значение в словарях на тип данных datetime. Подставляем "сегодняшний" год, что бы получить
        # дни рождения
        for k, val in i.items():
            val = [int(j) for j in val.split('-')]
            new_users_dict[k] = date(day=val[0], month=val[1], year=d_now.year)

    # Визначаємо дату від согоднящньої на неділю вперед
    d_week = d_now.date() + timedelta(weeks=1)
    # Визначаємо дату на 2 дні назад, потрібно для перевірки далі
    d_past_weekend = d_now.date() - timedelta(days=2)

    for k, v in new_users_dict.items():
        if d_now.date() <= v <= d_week:  # якщо дата дня народження в діапазоні сьогодні - неділя вперед
            day = v.weekday()  # Визначаємо в який день неділі день нар.
            if d_now.weekday() == 0 and (day == 5 or day == 6):  # Умова для того, щоб якщо сьогодні понеділок,
                # нашого іменинника внесло в список на наступний понеділок, а не в сьогодняшній
                weekdays_name[7].append(k)
            elif day == 5 or day == 6:  # Умова якщо др в вихідний, переносить привітання на понеділок
                weekdays_name[0].append(k)
            else:
                # Якщо не спрацювали попередні умови, просто додає іменинника в визначенний день
                weekdays_name[day].append(k)
        # Тут перевірка якщо сьогодня понеділок, перевіряє чи були іменинники на віхідних
        elif d_now.weekday() == 0 and (d_past_weekend <= v <= d_now.date()):
            weekdays_name[0].append(k)

    for day, names in weekdays_name.items():
        print(f'{weekdays_days[day]}: {"," .join(names)}')


get_birthday_per_week(users)
