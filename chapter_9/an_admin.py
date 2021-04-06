from admin import Admin, Privileges

admin = Admin('Jiawei', 'xing', 'a', 'b', 'c')
admin.describe_user()
admin.greet_user()
admin.increment_login_attempts()
admin.increment_login_attempts()
admin.reset_login_attempts()
admin.print_login_attempts()
admin.privileges.show_privileges()
