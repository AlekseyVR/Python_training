import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]  # для первого контакта
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    # print("\n", "home_lastname: ", contact_from_home_page.last_name_contact, "edit_lastname: ", contact_from_edit_page.last_name_contact)
    # print("\n", "home_firstname: ", contact_from_home_page.first_name_contact, "edit_firstname: ", contact_from_edit_page.first_name_contact)
    # print("\n", "home_email: ", contact_from_home_page.e_mail_contact, "edit_email: ", contact_from_edit_page.e_mail_contact)
    # print("\n", "home_email2: ", contact_from_home_page.e_mail_2_contact, "edit_email2: ", contact_from_edit_page.e_mail_2_contact)
    # print("\n", "home_email3: ", contact_from_home_page.e_mail_3_contact, "edit_email3: ", contact_from_edit_page.e_mail_3_contact)
    # print("\n", "home_address: ", contact_from_home_page.address_contact, "edit_address: ", contact_from_edit_page.address_contact)

    # print("\n", "home_home: ", contact_from_home_page.home_contact, "edit_home: ", contact_from_edit_page.home_contact)
    # print("\n", "home_work: ", contact_from_home_page.work_contact, "edit_work: ", contact_from_edit_page.work_contact)
    # print("\n", "home_mobile: ", contact_from_home_page.mobile_contact, "edit_mobile: ", contact_from_edit_page.mobile_contact)
    # print("\n", "home_secondary: ", contact_from_home_page.secondary_home, "edit_secondary: ", contact_from_edit_page.secondary_home)

    assert contact_from_home_page.last_name_contact == contact_from_edit_page.last_name_contact
    assert contact_from_home_page.first_name_contact == contact_from_edit_page.first_name_contact
    print("\n", "HP: ", contact_from_home_page.all_emails_from_home_page, "\n", "EP: ", merge_emails_like_on_home_page(contact_from_edit_page))
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.e_mail_contact == contact_from_edit_page.e_mail_contact
    # assert contact_from_home_page.e_mail_2_contact == contact_from_edit_page.e_mail_2_contact
    # assert contact_from_home_page.e_mail_3_contact == contact_from_edit_page.e_mail_3_contact

    assert contact_from_home_page.address_contact == contact_from_edit_page.address_contact

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.home_contact == contact_from_edit_page.home_contact
    # assert contact_from_home_page.work_contact == contact_from_edit_page.work_contact
    # assert contact_from_home_page.mobile_contact == contact_from_edit_page.mobile_contact
    # assert contact_from_home_page.secondary_home == contact_from_edit_page.secondary_home


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