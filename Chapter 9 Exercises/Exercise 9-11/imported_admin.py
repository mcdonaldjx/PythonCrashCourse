#Created 12/2/2022 by Jared
#Exercise 9-11- Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
from admin import Admin as adm
new_admin = adm('jared','m')
new_admin.privileges.show_privileges()
