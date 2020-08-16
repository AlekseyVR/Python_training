from sys import maxsize


class Contact:
    def __init__(self, first_name_contact=None, middle_name_contact=None, last_name_contact=None, nickname_contact=None,
                 title_contact=None, company_contact=None, address_contact=None, home_contact=None, mobile_contact=None,
                 work_contact=None,
                 fax_contact=None, e_mail_contact=None, e_mail_2_contact=None, e_mail_3_contact=None,
                 homepage_contact=None, birthday=None,
                 birthdmonth=None,
                 bYear=None, aDay=None, aMonth=None, aYear=None, secondary_address=None, secondary_home=None,
                 notes_contact=None, id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name_contact = first_name_contact
        self.middle_name_contact = middle_name_contact
        self.last_name_contact = last_name_contact
        self.nickname_contact = nickname_contact
        self.title_contact = title_contact
        self.company_contact = company_contact
        self.address_contact = address_contact
        self.home_contact = home_contact
        self.mobile_contact = mobile_contact
        self.work_contact = work_contact
        self.fax_contact = fax_contact
        self.e_mail_contact = e_mail_contact
        self.e_mail_2_contact = e_mail_2_contact
        self.e_mail_3_contact = e_mail_3_contact
        self.homepage_contact = homepage_contact
        self.birthday = birthday
        self.birthdmonth = birthdmonth
        self.bYear = bYear
        self.aDay = aDay
        self.aMonth = aMonth
        self.aYear = aYear
        self.secondary_address = secondary_address
        self.secondary_home = secondary_home
        self.notes_contact = notes_contact
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name_contact, self.last_name_contact)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name_contact == other.first_name_contact

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
