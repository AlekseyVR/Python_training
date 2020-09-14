import random
from models.contact import Contact
import pytest
import allure


def test_del_contacts(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if db.get_contact_list() == 0:
            app.contact.create(Contact(first_name_contact="For_delete"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact %s to the list' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
