from models.contact import Contact


def test_edit_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="For_edit"))
    app.contact.edit_first_contact(Contact(first_name_contact="NEWedit"))
