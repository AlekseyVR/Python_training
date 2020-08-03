from models.contact import Contact


def test_edit_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="For_edit"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(first_name_contact="NEWedit"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)