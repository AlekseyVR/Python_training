from models.contact import Contact


def test_edit_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="For_edit"))
    old_groups = app.group.get_group_list()
    app.contact.edit_first_contact(Contact(first_name_contact="NEWedit"))
    new_groups = app.group.get_group_list()
    assert (len(old_groups) == len(new_groups))