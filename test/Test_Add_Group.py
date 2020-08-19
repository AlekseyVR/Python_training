# -*- coding: utf-8 -*-
from models.group import Group
import pytest
import random
import string


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


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    # group = Group(name_group="first_group1", logo_group="first_logo2", footer_group="first_foot3")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# added second test with empty value
# def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name_group="", logo_group="", footer_group="")
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert (len(old_groups) + 1 == len(new_groups))
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
