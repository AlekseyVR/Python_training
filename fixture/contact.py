import time
import re
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
        self.contact_cache = None

    def confirm_create(self):
        wd = self.app.wd
        # confirm crete new contact
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def edit_contact_by_index(self, index, new_contact_data):
        # edit_some_contact
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.data_contact(new_contact_data)
        self.confirm_edit()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        # edit_some_contact
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("a[href='edit.php?id=%s" % id).click()
        self.data_contact(new_contact_data)
        self.confirm_edit()
        self.contact_cache = None

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0)
        # edit_contact - старый тест подготовлен для удаления
        # wd = self.app.wd
        # self.open_home_page()
        # wd.find_element_by_xpath("//img[@title='Edit']").click()
        # self.data_contact(new_contact_data)
        # self.confirm_edit()
        # self.contact_cache = None

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

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # submit some contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # submit alert
        wd.switch_to_alert().accept()
        time.sleep(3)
        # wd.find_element_by_css_selector("div.msgbox") - не помог, падает с ошибкой
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit some contact
        # wd.find_element_by_name("selected[]")[id].click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # submit alert
        wd.switch_to_alert().accept()
        time.sleep(3)
        # wd.find_element_by_css_selector("div.msgbox") - не помог, падает с ошибкой
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        # search all checkboxes on page
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                first_name_contact = element.find_elements_by_tag_name("td")[2].text
                last_name_contact = element.find_elements_by_tag_name("td")[1].text
                all_phones = element.find_elements_by_tag_name("td")[5].text
                address_contact = element.find_elements_by_tag_name("td")[3].text
                all_emails = element.find_elements_by_tag_name("td")[4].text
                self.contact_cache.append(
                    Contact(first_name_contact=first_name_contact, last_name_contact=last_name_contact, id=id,
                            all_phones_from_home_page=all_phones, address_contact=address_contact,
                            all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name_contact = wd.find_element_by_name("firstname").get_attribute("value")
        last_name_contact = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_contact = wd.find_element_by_name("home").get_attribute("value")
        work_contact = wd.find_element_by_name("work").get_attribute("value")
        mobile_contact = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_home = wd.find_element_by_name("phone2").get_attribute("value")
        address_contact = wd.find_element_by_name("address").get_attribute("value")
        e_mail_contact = wd.find_element_by_name("email").get_attribute("value")
        e_mail_2_contact = wd.find_element_by_name("email2").get_attribute("value")
        e_mail_3_contact = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name_contact=first_name_contact, last_name_contact=last_name_contact, id=id,
                       home_contact=home_contact, mobile_contact=mobile_contact, work_contact=work_contact,
                       secondary_home=secondary_home, address_contact=address_contact, e_mail_contact=e_mail_contact,
                       e_mail_2_contact=e_mail_2_contact, e_mail_3_contact=e_mail_3_contact)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_contact = re.search("H: (.*)", text).group(1)
        work_contact = re.search("W: (.*)", text).group(1)
        mobile_contact = re.search("M: (.*)", text).group(1)
        secondary_home = re.search("P: (.*)", text).group(1)
        return Contact(home_contact=home_contact, work_contact=work_contact, mobile_contact=mobile_contact,
                       secondary_home=secondary_home)
