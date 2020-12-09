f_distance = int(input('Введите количество километров, которое спортсмен пробежал в первый день '))
t_distance = int(input('Введите величину желаемой дистанции в километрах '))
c_distance = f_distance
n_day = 1
while c_distance <= t_distance:
    c_distance = c_distance + c_distance * 0.1
    n_day = n_day + 1
print('на', n_day, "день спортсмен будет пробегать", t_distance, "км")

