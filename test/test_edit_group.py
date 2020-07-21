from models.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name_group="first_group_e", logo_group="first_logo_e", footer_group="first_foot"))
    app.session.logout()