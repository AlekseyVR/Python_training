import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]  # для первого контакта
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    print("\n", "home_home: ", contact_from_home_page.home_contact, "edit_home: ", contact_from_edit_page.home_contact)
    print("\n", "home_work: ", contact_from_home_page.work_contact, "edit_work: ", contact_from_edit_page.work_contact)
    print("\n", "home_mobile: ", contact_from_home_page.mobile_contact, "edit_mobile: ",
          contact_from_edit_page.mobile_contact)
    print("\n", "home_secondary: ", contact_from_home_page.secondary_home, "edit_secondary: ",
          contact_from_edit_page.secondary_home)

    assert contact_from_home_page.home_contact == clear(contact_from_edit_page.home_contact)
    assert contact_from_home_page.work_contact == clear(contact_from_edit_page.work_contact)
    assert contact_from_home_page.mobile_contact == clear(contact_from_edit_page.mobile_contact)
    assert contact_from_home_page.secondary_home == clear(contact_from_edit_page.secondary_home)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_contact == contact_from_edit_page.home_contact
    assert contact_from_view_page.work_contact == contact_from_edit_page.work_contact
    assert contact_from_view_page.mobile_contact == contact_from_edit_page.mobile_contact
    assert contact_from_view_page.secondary_home == contact_from_edit_page.secondary_home


def clear(s):
    return re.sub("[() -]", "", s)
