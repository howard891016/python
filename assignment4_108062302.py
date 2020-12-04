import sys


class Record:
    """Represent a record."""

    def __init__(self, category, description, amount):
        self._category = category
        self._description = description
        self._amount = amount


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
                self._records.append([readin[0], ' ', readin[1], ' ', readin[2], '\n'])
        except:
            try:
                x = input('How much money do you have? ')
                self._init_money = int(x)
            except:
                sys.stderr.write('Invalid value for money. Set to 0 by default.\n')
                self._init_money = 0
            finally:
                self._records = []
