from models.group import Group


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name_group="New group"))


def test_edit_group_logo(app):
    app.group.edit_first_group(Group(logo_group="New logo"))
