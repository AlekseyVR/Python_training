# -*- coding: utf-8 -*-
from models.group import Group
import time


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name_group="new_group_3", logo_group="New_logo_3", footer_group="Footer_3"))
    app.session.logout()
    time.sleep(3)


# added second test with empty value
def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name_group="", logo_group="", footer_group=""))
    app.session.logout()
    time.sleep(3)
