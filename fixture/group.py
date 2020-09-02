from models.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # init group creation
        self.open_groups_page()
        wd.find_element_by_xpath("(//input[@name='new'])[2]").click()
        self.data_group(group)
        self.confirm_create()
        self.group_cache = None

    def confirm_create(self):
        wd = self.app.wd
        # To create a group
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # click edit button
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name('edit').click()
        # fill data group
        self.data_group(new_group_data)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self):
        self.modify_group_by_index(0)

    # def edit_first_group(self, new_group_data): заменен на новый edit_first_group
    #    wd = self.app.wd
    #    self.open_groups_page()
    #    # click edit button
    #    self.select_first_group()
    #    # open modification form
    #    wd.find_element_by_name('edit').click()
    #    # fill data group
    #    self.data_group(new_group_data)
    #    # submit
    #    wd.find_element_by_name("update").click()
    #    self.return_to_groups_page()
    #    self.group_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def data_group(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name_group)
        self.change_field_value("group_header", group.logo_group)
        self.change_field_value("group_footer", group.footer_group)

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion first group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion first group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    #  wd = self.app.wd
    #  self.open_groups_page()
    #  self.select_first_group()
    #  submit deletion first group
    #  wd.find_element_by_name("delete").click()
    #  self.return_to_groups_page()
    #  self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        # submit first group
        wd.find_elements_by_name("selected[]")[index].click()


    def select_group_by_id(self, id):
        wd = self.app.wd
        # submit first group
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def select_first_group(self):
        wd = self.app.wd
        # submit first group
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        # search all checkboxes on page
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name_group=text, id=id))
        return list(self.group_cache)
