# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    app.group.create()
    app.group.data_group(Group(name_group="first_group", logo_group="first_logo", footer_group="first_foot"))
    app.group.confirm_create()


# added second test with empty value
def test_add_empty_group(app):
    app.group.create()
    app.group.data_group(Group(name_group="", logo_group="", footer_group=""))
    app.group.confirm_create()
