from models.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    app.group.data_group(Group(name_group="edit_data", logo_group="edit_data", footer_group="edit_data"))
    app.group.confirm_edit()
    app.session.logout()