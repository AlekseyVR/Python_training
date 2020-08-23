from models.group import Group
import random
import string

# для исп константы в тесте изменить импорт на: from data.add_group import constant as testdata
constant = [
    Group(name_group="Name1", logo_group="logo1", footer_group="footer1"),
    Group(name_group="Name2", logo_group="logo2", footer_group="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name_group="", logo_group="", footer_group="")] + [
    # Group(name_group="first_group1", logo_group="first_logo2", footer_group="first_foot3"),
    # Group(name_group="", logo_group="", footer_group=""),
    Group(name_group=random_string("name", 10), logo_group=random_string("logo", 20),
          footer_group=random_string("footer", 10))

    # Group(name_group=name_group, logo_group=logo_name, footer_group=footer_group)

    for i in range(2)
    # for name_group in ['', random_string('name', 10)]
    # for logo_name in ['', random_string('logo', 10)]
    # for footer_group in ['', random_string('footer', 10)]
]
