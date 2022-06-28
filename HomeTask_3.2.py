def p_inf(name, s_name, b_year, city, email, mob):
        return f'Имя - {name}; фамилия - {s_name}; год рождения - {b_year}; город проживания - {city}; эл. почта - {email}; номер телефона - {mob}'

print(p_inf(name = 'Harry', s_name = 'Potter', b_year = '1980', city = 'Little Whinging',
            email = 'theboywholived@gmail.com', mob = '856-124-5423'))