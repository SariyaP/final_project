# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file
import copy
import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def open_csv(name, file):
    name = []
    with open(os.path.join(__location__, f'{file}.csv')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            name.append(dict(r))
    return name

def write(name, file, my_db):
    table = my_db.search(name.split('.')[0])
    if table.table.__len__() > 0:
        with open(os.path.join(__location__, f'{file}.csv'), 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=table.table[0].keys())
            writer.writeheader()
            for row in table.table:
                writer.writerow(row)


# add in code for a Database class
class DB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


# add in code for a Table class
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def insert(self, table):
        self.table.append(table)

    def delete(self, value):
        for i in range(len(self.table)):
            if 'ID' in self.table:
                if self.table[i]['ID'] == value:
                    del self.table[i]
                    break
            else:
                if self.table[i]['ProjectID'] == value:
                    del self.table[i]
                    break


    def update_table(self, key, value):
        self.table[0].update({f"{key}": f"{value}"})

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
