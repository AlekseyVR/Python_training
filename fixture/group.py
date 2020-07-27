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

    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # click edit button
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_name('edit').click()

    def data_group(self, group):
        wd = self.app.wd
        # editing data
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name_group)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.logo_group)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer_group)

    def confirm_edit(self):
        wd = self.app.wd
        # send edit data group
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # submit first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion first group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
