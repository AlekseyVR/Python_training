import random
import bdd
from models.group import Group



def test_delete_some_group(app, db, check_ui):
    # если число чек-боксов группы равно нулю, то создаем группу
    # if app.group.count() == 0:
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name_group="test_for_Del"))
    # удаляем группу
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id)
    # app.group.delete_group_by_index(index) через бд не годится

    new_groups = db.get_group_list()
    assert (len(old_groups) - 1 == len(new_groups))  # можно ее удалить, но останется для пустых спиков или др. проблем
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
