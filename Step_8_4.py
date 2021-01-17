"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
 А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
 определить параметры, общие для приведенных типов. В классах-наследниках реализовать
  параметры, уникальные для каждого типа оргтехники."""

class Sklad:
    def __init__(self, sk_name):
        self.sk_name = sk_name

class Nomenclature:
    def __init__(self,inv_num,  model, brand, quantity, intreface, *other):
        self.inv_num = inv_num
        self.price = model
        self.brand = brand
        self.quantity = quantity
        self.net = intreface
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'inv_num': self.inv_num, 'model': self.model, 'brand': self.brand,
                        'quantity': self.quantity, 'intreface': self.intreface}

        def date_input(self):

            try:
                u_inv_num = input(f' Введите инвентарный номер')
                u_model = input(f'Введите наименование модели ')
                u_brand = input(f'Введите наименование производителя')
                u_quantity = int(input(f'Введите количество '))
                u_intreface = input(f'Введите интерфейс оборудования')
                unique = {'inv_num': u_inv_num,'brand': u_brand, 'model': u_model,
                        'quantity': u_quantity, 'intreface': u_intreface}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                print(f'Текущий список -\n {self.my_store}')
            except:
                return f'Ошибка при вводе количества'

            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q.lower() == 'q':
                self.my_store_full.append(self.my_store)
                print(f'полный перечень -\n {self.my_store_full}')
                return f'выход'
            else:
                return Nomenclature.reception(self)


class Printer(Nomenclature):
    def __init__(self, inv_num,  model, brand, quantity, intreface, cartrige, color):
        Nomenclature.__init__(self, inv_num,  model, brand, quantity, intreface)
        self.cartrige = cartrige
        self.color = False
    def printed(self):
            return f'оборудование {self.model} под номером {self.inv_num} принтер'


class Scaner(Nomenclature):

    def __init__(self, inv_num,  model, brand, quantity, intreface, type):
        Nomenclature.__init__(self, inv_num, model, brand, quantity, intreface)
        self.type = type
    def scan(self):
        return f'оборудование {self.model} под номером {self.inv_num} сканер'

class Copier(Nomenclature):

    def __init__(self, inv_num, model, brand, quantity, intreface, cartrige, color, type ):
        Nomenclature.__init__(self, inv_num, model, brand, quantity, intreface)
        self.cartrige = cartrige
        self.color = False
        self.type = type

    def copyed(self):
        return f'оборудование {self.model} под номером {self.inv_num} копир'

u_1 = Printer('B-021','lj-3600','hp', 2, "USB", "ct804A", False)
u_2 = Scaner('S-012','lbp-1200','canon', 1, "USB", "lingering")
u_3 = Copier('O-008','kd-127','brother', 3, "USB", "qx61", False, 'tablet')
print(u_1.date_input())
print(u_2.date_input())
print(u_3.date_input())
print(u_1.printed())
print(u_3.copyed())