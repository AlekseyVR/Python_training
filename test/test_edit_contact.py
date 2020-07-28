from models.contact import Contact


def test_edit_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name_contact="NEW", middle_name_contact="middle_name_contact",
                                   last_name_contact="last_name_contact", nickname_contact="nickname_contact",
                                   title_contact="title_contact", company_contact="company_contact",
                                   address_contact="address_contact", home_contact="Home_contact",
                                   mobile_contact="Mobile_contact",
                                   work_contact="Work_contact", fax_contact="Fax_contact",
                                   e_mail_contact="E-mail_contact", e_mail_2_contact="E-mail_contact_2",
                                   e_mail_3_contact="E-mail_contact_3",
                                   homepage_contact="Homepage_contact", birthday="2", birthdmonth="January",
                                   bYear="1994", aDay="20", aMonth="December", aYear="1995",
                                   secondary_address="secondary_address_contact",
                                   secondary_home="secondary_home_contact", notes_contact="Notes_contact"))
    app.contact.edit_contact(Contact(first_name_contact="edit", middle_name_contact="edit",
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
