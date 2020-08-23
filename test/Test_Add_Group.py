# -*- coding: utf-8 -*-
from models.group import Group
import pytest
from data.add_group import constant as testdata


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
