import requests

URL = "https://fakerestapi.azurewebsites.net"

authors = requests.get(f"{URL}/api/v1/Authors")
print(authors.json())

author_id = requests.get(f"{URL}/api/v1/Authors/10")
print(author_id.json())

data_new_book = {
    "id": 156562,
    "title": "Gambardella, Matthew",
    "description": "An in-depth look at creating applications with XML",
    "pageCount": 150,
    "publishDate": "2000-10-11T05:12:01"
}
add_new_book = requests.post(f"{URL}/api/v1/Books", json=data_new_book)
print(add_new_book.json())

data_new_user = {
    "id": 145,
    "email": 'Bob@gmail.com',
    "userName": 'Bob',
    "password": 'qwerty'
}

add_new_user = requests.post(f"{URL}/api/v1/Users", json=data_new_user)
print(add_new_user.json())

data_book = {

    'id': 189,
    "title": "Clean Code",
    "description": "Even bad code can function. But if code isn’t clean, "
                   "it can bring a development organization to its knees.",
    "pageCount": 250,
    "publishDate": "2008-09-10T12:00:00"

}

update_book_10 = requests.put(f"{URL}/api/v1/Books/10", json=data_book)
print(update_book_10.json())

drop_user = requests.delete(f"{URL}/api/v1/Users/4")
print(drop_user.status_code)
