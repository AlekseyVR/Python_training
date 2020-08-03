from models.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name_group="test_for_ed_nm_grp"))

    old_groups = app.group.get_group_list()
    group = Group(name_group="New group")
    app.group.edit_first_group(group)
    group.id = old_groups[0].id
    # app.group.edit_first_group(Group(name_group="New group"))
    new_groups = app.group.get_group_list()
    assert (len(old_groups) == len(new_groups))
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_edit_group_logo(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name_group="test_for_ed_lg_grp"))
#
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(logo_group="New logo"))
#    new_groups = app.group.get_group_list()
#    assert (len(old_groups) == len(new_groups))
