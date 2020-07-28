from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        # create_contact
        wd = self.app.wd
        self.return_nav_home()
        wd.find_element_by_link_text("add new").click()
        self.data_contact(contact)
        self.confirm_create()
        self.return_nav_home()

    def confirm_create(self):
        wd = self.app.wd
        # confirm crete new contact
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def edit_first_contact(self, new_contact_data):
        # edit_contact
        wd = self.app.wd
        self.return_nav_home()
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

    def return_nav_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text('home').click()

    def confirm_edit(self):
        wd = self.app.wd
        # confirm editing contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_nav_home()
        # submit first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # submit alert
        wd.switch_to_alert().accept()
        self.return_nav_home()

    def count(self):
        wd = self.app.wd
        self.return_nav_home()
        # search all checkboxes on page
        return len(wd.find_elements_by_name("selected[]"))
