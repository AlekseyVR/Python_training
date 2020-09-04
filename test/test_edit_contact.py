from random import randrange
import random
from models.contact import Contact


def test_edit_contacts(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="For_edit"))
    old_contacts = db.get_contact_list()
    # index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    # contact = Contact(first_name_contact="Edit_first_name")
    new_contact_data = Contact(first_name_contact="Edit_first_name")
    app.contact.edit_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contact_list()
    # contact.id = old_contacts[index].id
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    contact.first_name_contact = new_contact_data.first_name_contact
    # old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    print("old_contacts: \n", old_contacts)
    print("new_contacts: \n", new_contacts)
