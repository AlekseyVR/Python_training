# -*- coding: utf-8 -*-

from contact import Contact
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contacts(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name_contact="first_name_contact", middle_name_contact="middle_name_contact",
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
    app.logout()
