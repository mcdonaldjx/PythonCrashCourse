#Created 12/2/2022 by Jared
#Exercise 9-12- Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
from admin import Admin as adm
new_admin = adm('jared','m')
new_admin.privileges.show_privileges()
