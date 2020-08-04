from random import randrange

from models.contact import Contact


def test_edit_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="For_edit"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name_contact="Edit_first_name")
    app.contact.edit_contact_by_index(index, contact)

    contact.id = old_contacts[index].id
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
