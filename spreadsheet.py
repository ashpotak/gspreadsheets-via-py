import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
 
# Авторизація
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Знаходимо файл за ім'ям та відкриваємо першу таблицю
sheet = client.open("spreadsheet").sheet1
 
# Виводимо всі дані
list_of_values = sheet.get_all_values()
print(list_of_values)
