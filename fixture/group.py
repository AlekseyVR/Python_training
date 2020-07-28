class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create(self):
        wd = self.app.wd
        # init group creation
        self.open_groups_page()
        wd.find_element_by_xpath("(//input[@name='new'])[2]").click()

    def confirm_create(self):
        wd = self.app.wd
        # To create a group
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # click edit button
        self.select_first_group()
        # open modification form
        wd.find_element_by_name('edit').click()
        # fill data group
        self.data_group(new_group_data)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

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

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion first group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        # submit first group
        wd.find_element_by_name("selected[]").click()
