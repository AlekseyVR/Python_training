import re
from models.contact import Contact
from random import randrange


def test_contact_data_for_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="XXX", last_name_contact="ZZZZ", address_contact="Home",
                                   work_contact="1234455", e_mail_contact="test@test.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # firstname
    assert contact_from_home_page.first_name_contact == contact_from_edit_page.first_name_contact
    # lastname
    assert contact_from_home_page.last_name_contact == contact_from_edit_page.last_name_contact
    # address
    assert contact_from_home_page.address_contact == contact_from_edit_page.address_contact
    # phones
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # emails
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

    print("\n", "HP: ", contact_from_home_page.all_emails_from_home_page, "\n", "EP: ",merge_emails_like_on_home_page(contact_from_edit_page))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_contact, contact.mobile_contact, contact.work_contact,
                                        contact.secondary_home]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.e_mail_contact, contact.e_mail_2_contact, contact.e_mail_3_contact]))))


def test_contact_db_info_matches_ui(app, db):
    ui_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(id=contact.id, first_name_contact=contact.first_name_contact,
                       last_name_contact=contact.last_name_contact,
                       address_contact=contact.address_contact,
                       all_phones_from_home_page=merge_phones_like_on_home_page(contact),
                       all_emails_from_home_page=merge_emails_like_on_home_page(contact))

    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
