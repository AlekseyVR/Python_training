from random import randrange
import random
from models.contact import Contact
import pytest
import allure


def test_edit_contacts(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(first_name_contact="For_edit"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('Given a contact with new data'):
        new_contact_data = Contact(first_name_contact="Edit_first_name")
    with allure.step('When I enter new contact data'):
        app.contact.edit_contact_by_id(contact.id, new_contact_data)
    with allure.step('Then the new contact list is equal to the old list with modified contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == app.contact.count()
        contact.first_name_contact = new_contact_data.first_name_contact
        # old_contacts[index] = contact
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        print("old_contacts: \n", old_contacts)
        print("new_contacts: \n", new_contacts)
