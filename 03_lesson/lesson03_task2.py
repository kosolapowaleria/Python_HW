from smartphone import Smartphone

catalog = [Smartphone('Samsung', 'Galaxy S25', '+79...'),
           Smartphone('Apple', 'Iphone 16', '+79...'),
           Smartphone('Nokia', '3310', '+79...'),
           Smartphone('Xiaomi', '14T Pro', '+79...'),
           Smartphone('Realme', 'GT7 Pro', '+79...')]

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')