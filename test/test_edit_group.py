from models.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name_group="test_for_ed_nm_grp"))
    app.group.edit_first_group(Group(name_group="New group"))


def test_edit_group_logo(app):
    if app.group.count() == 0:
        app.group.create(Group(name_group="test_for_ed_lg_grp"))
    app.group.edit_first_group(Group(logo_group="New logo"))
