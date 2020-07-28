from models.group import Group


def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name_group="New group"))
    app.session.logout()


def test_edit_group_logo(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(logo_group="New logo"))
    app.session.logout()
