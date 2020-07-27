from models.contact import Contact


def test_add_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact()
    app.contact.data_contact(Contact(first_name_contact="edit", middle_name_contact="edit",
                                     last_name_contact="edit", nickname_contact="edit",
                                     title_contact="edit", company_contact="edit",
                                     address_contact="edit", home_contact="edit",
                                     mobile_contact="edit",
                                     work_contact="edit", fax_contact="edit",
                                     e_mail_contact="E-edit", e_mail_2_contact="E-edit",
                                     e_mail_3_contact="E-edit",
                                     homepage_contact="edit", birthday="2", birthdmonth="January",
                                     bYear="1994", aDay="20", aMonth="December", aYear="1995",
                                     secondary_address="edit",
                                     secondary_home="edit", notes_contact="edit"))
    app.contact.confirm_edit()
    app.session.logout()
