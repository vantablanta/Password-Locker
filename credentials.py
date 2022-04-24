class Credentials:
    """
    class that defines the password object
    """
    def __init__(self, password):
        self.password = password        


    def save_password(self, password):
        """
        Function to add passwords
        """
    

password1 = Credentials('1234')