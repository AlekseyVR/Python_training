from models.contact import Contact


def test_add_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(first_name_contact="edited", middle_name_contact="edited",
                                     last_name_contact="edited", nickname_contact="edited",
                                     title_contact="edited", company_contact="edited",
                                     address_contact="edited", home_contact="edited",
                                     mobile_contact="edited",
                                     work_contact="edited", fax_contact="edited",
                                     e_mail_contact="edited", e_mail_2_contact="edited",
                                     e_mail_3_contact="edited",
                                     homepage_contact="edited", birthday="1", birthdmonth="January",
                                     bYear="1993", aDay="2", aMonth="December", aYear="1996",
                                     secondary_address="edited",
                                     secondary_home="edited", notes_contact="edited"))
    app.session.logout()
