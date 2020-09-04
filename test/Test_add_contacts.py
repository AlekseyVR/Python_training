# -*- coding: utf-8 -*-

from models.contact import Contact
#import pytest
#from data.add_contact import constant as testdata


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    # assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
