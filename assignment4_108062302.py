import sys


class Record:
    """Represent a record."""

    def __init__(self, category, description, amount,num):
        self._category = category
        self._description = description
        self._amount = amount
        self._num = num
    @property
    def category(self):
        return self._category
    @property
    def description(self):
        return self._description
    @property
    def amount(self):
        return self._amount
    @property 
    def num(self):
        return self._num

class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""

    def __init__(self):
        try:
            fh = open('records.txt')
            try:
                read = fh.readline()
                if read.isspace():
                    print(error)
            except:
                sys.stderr.write('No line is in the file!\n')
                self._init_money = 0
                self._records = []
            finally:
                initial = read.split(' ')
            try:
                self._init_money = int(initial[1])
            except:
                sys.stderr.write('Invalid initial money in file! Initial it as 0!\n')
                self._init_money = 0
            finally:
                self._records = []
            for i in fh.readlines():
                readin = i.split(' ')
                self._records.append(
                    [readin[0], ' ', readin[1], ' ', readin[2], '\n'])
        except:
            try:
                x = input('How much money do you have? ')
                self._init_money = int(x)
            except:
                sys.stderr.write('Invalid value for money. Set to 0 by default.\n')
                self._init_money = 0
            finally:
                self._records = []

    def add(self, record, categories):
        readin = record.split(' ')
        p = categories.is_category_valid(readin[0])
        if p == True:
            num = 1
            for i in self._records:
                if i.description == readin[1]:
                    num += 1
            be_add = Record(readin[0], readin[1], int(readin[2]), num)
            self._records.append(be_add)
        else:
            print('The specified category is not in the category list.')
            print('You can check the category list by command "view categories".')
            print('Fail to add a record.')

    def view(self):
        print("Here's your expense and income record:")
        print('{:<15s}{:<15s}{:<10s}'.format('Category', 'Description', 'Amount'))
        print('=============  =============  ==========')
        for i in self._records:
            print('{:<15s}{:<15s}{:10d}'.format(i.category, i.description, i.amount))
        want = self._init_money
        for i in self._records:
            want = want + i.amount
        print('Now you have {:>6d} money left!'.format(want))

    def delete(self,delete_record):
        flag = False
        quan = 0
        for i in self._records:
            if i.description == delete_record:
                quan += 1
                flag = True
        if flag == False:
            print('No such record. Fail to delete record')
        if quan > 1:
            print('Which record do you want to delete')
            for i in self._records:
                if i.description == delete_record:
                    print('{:<2d}{:<15s}{:15s}{:<10d}'.format(i.num,i.category,i.description,i.amount))
            x = input('Type in the number: ')
            for i in self._records:
                if i.description == delete_record and int(x) == i.num:
                    count = self._records.index(i)
                    del(self._records[count])
        else:
            for i in self._records:
                if i.description == delete_record:
                    count = self._records.index(i)
                    del(self._records[count])
        

class Categories:
    """Maintain the category list and provide some methods."""

    def __init__(self):
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', [
            'bus', 'railway']], 'income', ['salary', 'bonus']]

    def view(self):
        def inner_recursive(L, level=0):
            if L == None:
                return
            if type(L) in {list, tuple}:
                for child in L:
                    inner_recursive(child, level+1)
            else:
                s = ' '*2*level
                s += '- ' + L
                print(s)

        inner_recursive(self._categories)

    def is_category_valid(self, category):
        def valid(L, want):
            if type(L) in {list, tuple}:
                for v in L:
                    p = valid(v, want)
                    if p == True:
                        return p
            return L == want

        return valid(self._categories, category)


categories = Categories()
records = Records()

while True:
    command = input(
        '\nWhat do you want to do (add / view / delete / view categories / find / exit)? ')
    if command == 'add':
        record = input(
            'Add an expense or income record with category, description, and amount (separate by spaces):\n')
        records.add(record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view()
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')
