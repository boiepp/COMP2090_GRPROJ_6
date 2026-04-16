class User:
    def __init__(self, user_id, name, phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone
    
    def get_user_id(self):
        return self.user_id
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
