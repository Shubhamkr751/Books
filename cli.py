import requests

BASE_URL = 'http://127.0.0.1:5000'

def create_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    publication_year = input("Enter publication year: ")

    data = {
        "title": title,
        "author": author,
        "genre": genre,
        "publication_year": int(publication_year)
    }

    response = requests.post(f'{BASE_URL}/books', json=data)
    print(response.json())

def retrieve_book():
    book_id = input("Enter book ID: ")
    response = requests.get(f'{BASE_URL}/books/{book_id}')
    print(response.json())

def list_books():
    response = requests.get(f'{BASE_URL}/books')
    print(response.json())

def update_book():
    book_id = input("Enter book ID to update: ")
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    genre = input("Enter new genre: ")
    publication_year = input("Enter new publication year: ")

    data = {
        "title": title,
        "author": author,
        "genre": genre,
        "publication_year": int(publication_year)
    }

    response = requests.put(f'{BASE_URL}/books/{book_id}', json=data)
    print(response.json())

def delete_book():
    book_id = input("Enter book ID to delete: ")
    response = requests.delete(f'{BASE_URL}/books/{book_id}')
    print(response.json())

def main():
    while True:
        print("\nChoose an option:")
        print("1. Create Book")
        print("2. Retrieve Book")
        print("3. List Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            create_book()
        elif choice == '2':
            retrieve_book()
        elif choice == '3':
            list_books()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
