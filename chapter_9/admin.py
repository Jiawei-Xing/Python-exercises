from user import User


class Admin(User):
    """初始化子类"""
    def __init__(self, first_name, last_name, *privileges):
        """把子类两个变量关联到父类"""
        super().__init__(first_name, last_name)
        """把列表变量privileges应用到Priviliges类中，并将这个实例储存为Admin的属性"""
        self.privileges = Privileges(privileges)
        

class Privileges():
    def __init__(self, *privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        print("\nPrivileges: ")
        for privilege in self.privileges:
            print(privilege)


