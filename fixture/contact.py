from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        # create_contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name_contact)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name_contact)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name_contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname_contact)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title_contact)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_contact)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address_contact)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_contact)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_contact)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_contact)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_contact)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.e_mail_contact)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.e_mail_2_contact)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.e_mail_3_contact)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage_contact)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthdmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.bYear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aDay)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.aMonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.aYear)
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_home)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes_contact)
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def return_home_page(self):
        # return_home_page
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def return_nav_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text('home').click()

    def delete_first_contact(self):
        wd = self.app.wd
        # submit first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # submit alert
        wd.switch_to_alert().accept()
        self.return_nav_home()
