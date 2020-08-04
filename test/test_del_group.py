from random import randrange
from models.group import Group


def test_delete_some_group(app):
    # если число чек-боксов группы равно нулю, то создаем группу
    if app.group.count() == 0:
        app.group.create(Group(name_group="test_for_Del"))
    # удаляем группу
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert (len(old_groups) - 1 == len(new_groups))  # можно ее удалить, но останется для пустых спиков или др. проблем
    old_groups[index:index+1] = []
    assert old_groups == new_groups
