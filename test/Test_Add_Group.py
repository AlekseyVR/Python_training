# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name_group="first_group", logo_group="first_logo", footer_group="first_foot"))
    new_groups = app.group.get_group_list()
    assert (len(old_groups) + 1 == len(new_groups))


# added second test with empty value
def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name_group="", logo_group="", footer_group=""))
    new_groups = app.group.get_group_list()
    assert (len(old_groups) + 1 == len(new_groups))
