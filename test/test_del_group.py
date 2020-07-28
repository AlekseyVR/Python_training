from models.group import Group


def test_delete_first_group(app):
    # если число чек-боксов группы равно нулю, то создаем группу
    if app.group.count() == 0:
        app.group.create(Group(name_group="test_for_Del"))
    # удаляем группу
    app.group.delete_first_group()
