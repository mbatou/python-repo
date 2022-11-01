from abc import ABC, abstractmethod

class ProductAbstract:
    create_product = ''
    edit_product = ''
    get_product_by_id = ''
    get_all_product = ''
    upload_product_image = ''
    delete_product = ''

class ProductManager():
    @abstractmethod
    def get_product_by_id(self):
        pass
    def edit_product(self):
        pass
    def create_product(self):
        pass
    def get_all_product(self):
        pass
    def upload_product_image(self):
        pass
    def delete_product(self):
        pass

class trainee():
    def maintenance(self):
        print("Doing my job")

new_tenant = ProductManager()
new_tenant.edit_product()
