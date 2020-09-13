Scenario Outline: Add new group
  Given a group list
  Given a group with <name_group>, <logo_group> and <footer_group>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
| name_group | logo_group | footer_group |
| name1 | logo1 | footer1 |
| name2 | logo2 | footer2 |

Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old list without the deleted group

