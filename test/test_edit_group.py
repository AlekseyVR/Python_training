import random
from models.group import Group


def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name_group="test_for_ed_nm_grp"))
    old_groups = db.get_group_list()

    group = random.choice(old_groups)
    new_group_data = Group(name_group="Modify group")
    app.group.modify_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    group.name = new_group_data.name_group
    assert old_groups == new_groups

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
