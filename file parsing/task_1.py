import xml.etree.ElementTree as ET

tree = ET.parse("library.xml")
root = tree.getroot()


# search by author
for book in root.findall('book'):
    for author in book.findall('author'):
        book_author = author.text
        if "Ga" in book_author:
            print(book.attrib)
            for name in book:
                print(name.text)

# search by price
for book in root.findall('book'):
    for price in book.findall('price'):
        book_price = price.text
        if "17" in book_price:
            print(book.attrib)
            for name in book:
                print(name.text)

# search by tittle
for book in root.findall('book'):
    for title in book.findall('title'):
        book_title = title.text
        if "Maeve" in book_title:
            print(book.attrib)
            for name in book:
                print(name.text)

# search by description
for book in root.findall('book'):
    for description in book.findall('description'):
        book_description = description.text
        if "A former architect " in book_description:
            print(book.attrib)
            for name in book:
                print(name.text)
