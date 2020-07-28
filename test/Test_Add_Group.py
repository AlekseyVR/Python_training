# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    app.group.create(Group(name_group="first_group", logo_group="first_logo", footer_group="first_foot"))


# added second test with empty value
def test_add_empty_group(app):
    app.group.create(Group(name_group="", logo_group="", footer_group=""))
