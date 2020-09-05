from models.contact import Contact
from models.group import Group
import random


def test_add_contact_to_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create(Contact(first_name_contact="contact_in_group"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    available_groups = orm.get_groups_not_containing_contact(contact)
    if not available_groups:
        group = Group(name_group="Contact_in_Group")
        app.group.create(group)
    else:
        group = random.choice(available_groups)
    app.contact.add_contact_to_group(contact.id, group.id, group.name_group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group
