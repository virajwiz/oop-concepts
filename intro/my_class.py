class MyClass:
    def __init__(self, data):
        self.__data = data
        self.public_member = "Public Member"
        self.__private_member = "Private Member"
        self._protected_member = "Protected Member"
    

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    def public_method(self):
        print("Public Method")

    def _protected_method(self):
        print("Protected Method")


class Subclass(MyClass):
    def __init__(self, data):
        super().__init__(data)
        
    def access_protected(self):
        print(self._protected_member)
        self._protected_method()




        