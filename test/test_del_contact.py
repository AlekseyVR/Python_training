from models.contact import Contact


def test_del_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="For_delete"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)

