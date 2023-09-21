from peewee import *

db = SqliteDatabase('Records.sqlite')


class Record(Model):
    name = CharField()
    score = CharField()
    country = CharField()


class meta:
    database = db


def __str__(self):
    return f'{self.name} has this {self.score} and from {self.country}'


db.connect()
db.create_tables([Record])


def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    print('todo display all records')

    print('\n The records are here ')

    harry = Record(name="Harry", score=32, country="France")
    harry.save()

    Margo = Record(name="Margo", score=29, country="Brazil")
    Margo.save()
    Sammy = Record(name="Sammy", score=44, country="United kingdom")
    Sammy.save()
    Clone = Record(name="Clone", score=43, country="United States")
    Clone.save()

    print('\nFind all records')
    records = Record.select()
    for Records in Record:
        print(records)


def search_by_name():
    print(
        'todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')

    print('\nRecord, are sorted by name')
    for Records in Record.select().order_byname(Record.name):
        print(Record)


def add_new_record():
    print('todo add new record. What if user wants to add a record that already exists?')

    Clone_id = Clone.id
    Clone = Record.get_by_id(Clone_id)
    print(f'\n get by id {Clone_id} returns:', Clone)


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?')
    harry.score = 34
    harry.save()
    print('\nharry is now:', Harry)


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?')

    print('\n deleting name')
    row_deleted = Record.delete().where(Record.name == 'Sammy').excute()
    print('Rows deleted:', row_deleted)


if __name__ == '__main__':
    main()
