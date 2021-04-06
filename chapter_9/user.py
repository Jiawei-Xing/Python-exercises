class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name.title() + " " + self.last_name.title()
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.full_name)
        
    def greet_user(self):
        print("Hello, " + self.full_name + "!")
        
    def print_login_attempts(self):
        print("login attempts: " + str(self.login_attempts))
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0    
