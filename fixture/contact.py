import time

from selenium.webdriver.support.select import Select
from models.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text('home').click()

    def create(self, contact):
        # create_contact
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.data_contact(contact)
        self.confirm_create()
        self.open_home_page()

    def confirm_create(self):
        wd = self.app.wd
        # confirm crete new contact
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def edit_first_contact(self, new_contact_data):
        # edit_contact
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.data_contact(new_contact_data)
        self.confirm_edit()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_selector_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def data_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name_contact)
        self.change_field_value("middlename", contact.middle_name_contact)
        self.change_field_value("lastname", contact.last_name_contact)
        self.change_field_value("nickname", contact.nickname_contact)
        self.change_field_value("title", contact.title_contact)
        self.change_field_value("company", contact.company_contact)
        self.change_field_value("address", contact.address_contact)
        self.change_field_value("home", contact.home_contact)
        self.change_field_value("mobile", contact.mobile_contact)
        self.change_field_value("work", contact.work_contact)
        self.change_field_value("fax", contact.fax_contact)
        self.change_field_value("email", contact.e_mail_contact)
        self.change_field_value("email2", contact.e_mail_2_contact)
        self.change_field_value("email3", contact.e_mail_3_contact)
        self.change_field_value("homepage", contact.homepage_contact)
        self.change_selector_value("bday", contact.birthday)
        self.change_selector_value("bmonth", contact.birthdmonth)
        self.change_field_value("byear", contact.bYear)
        self.change_selector_value("aday", contact.aDay)
        self.change_selector_value("amonth", contact.aMonth)
        self.change_field_value("ayear", contact.aYear)
        self.change_field_value("address2", contact.secondary_address)
        self.change_field_value("phone2", contact.secondary_home)
        self.change_field_value("notes", contact.notes_contact)

    def return_home_page(self):
        # return_home_page
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def confirm_edit(self):
        wd = self.app.wd
        # confirm editing contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # submit first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # submit alert
        wd.switch_to_alert().accept()
        time.sleep(3)
        # wd.find_element_by_css_selector("div.msgbox") - не помог, падает с ошибкой
        self.open_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        # search all checkboxes on page
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contact_list = []
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            first_name_contact = element.find_elements_by_tag_name("td")[2].text
            last_name_contact = element.find_elements_by_tag_name("td")[1].text
            contact_list.append(
                Contact(first_name_contact=first_name_contact, last_name_contact=last_name_contact, id=id))
        return contact_list
