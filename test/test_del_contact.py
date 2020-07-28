from models.contact import Contact


def test_del_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="For_delete"))
    app.contact.delete_first_contact()
