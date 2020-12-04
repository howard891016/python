import sys
import os

def add(record):
    try:
        typein = input('Add an expense or income record with description and amount:\n')
        read = typein.split()
        item = read[0]
        try:
            if read[1]:
                print('',end = '')
        except:
            sys.stderr.write('String cannot be split into two strings.\n')
            return record
        money = int(read[1])
        num = 0
        for i in record:
            if i[0] == item:
                num = num + 1
        record.append([item,' ',read[1],' ',str(num),'\n'])
    except ValueError:
        sys.stderr.write('Invalid value for money! Fail to add a record.\n')
    return record

def delete(record):
    item = input('Which record do you want to delete? ')
    cnt = 0
    quan = 0
    for i in record:
        if i[0] == item:
            quan = quan + 1
    if quan > 1:
        print('Which one do you want to delete?')
        for i in record:
            if item == i[0]:
                print('{:>2s}.{:<10s}{:<10s}'.format(i[4],i[0],i[2]))
        x = input('Type in the number: ')
        for i in record:
            if item == i[0] and x == i[4]:
                count = record.index(i)
                del(record[count])
                return record
    for i in record:
        cnt = cnt + 1
        if(i[0] == item):
            count = record.index(i)
            del(record[count])
            return record
    for i in record:
        cnt = cnt + 1
        if(i[0] == item):
            count = record.index(i)
            del(record[count])
            return record
    try:
        if(cnt == len(record)):
            print(error)
    except:
        sys.stderr.write('The specified record does not exist.\n')
    return record

def view(init,record):
    print("Here's your expense and income record:")
    print('{:<20s}{:<10s}'.format('Description','Amount'))
    for i in range(0,17):
        print('=',end = '')
    for i in range(17,20):
        print(' ',end = '')
    for i in range(20,30):
        print('=',end = '')
    print('')
    for i in record:
        print('{:<20s}{:<10s}'.format(i[0],i[2]))
        for j in range(0,30):
            print('=',end = '')
        print('')
    want = init
    for i in record:
        money = int(i[2])
        want = want + money
    print('Now you have {:>6d} money left!'.format(want))

def initialize():
    try:
        fh = open('records.txt')
        try:
            read = fh.readline()
            if read.isspace():
                print(error)
        except:
            sys.stderr.write('No line is in the file!\n')
            money = 0
            record = []
            return money, record
        initial = read.split(' ')
        try:
            money = int(initial[1])
        except:
            sys.stderr.write('Invalid initial money in file! Initial it as 0!\n')
            money = 0
            record = []
            return money , record
        record = []
        for i in fh.readlines():
            readin = i.split(' ')
            record.append([readin[0],' ',readin[1],' ',readin[2],'\n'])
    except:
        try:
            x = input('How much money do you have? ')
            money = int(x)
            record = []
        except:
            sys.stderr.write('Invalid value for money. Set to 0 by default.\n')
            record = []
            money = 0
    return money, record

def save(init, record):
    want = init
    fh = open('records.txt','w')
    for i in record:
        money = int(i[2])
        want = want + money
    fh.writelines(['init',' ', str(want),'\n'])
    for i in record:
        fh.writelines(i)
    fh.close()

init_money , records = initialize()

while True:
    command = input('What do you want to do (add / view / delete / exit)? ')

    if command == 'add':
        records = add(records)
    elif command == 'view':
        view(init_money,records)
    elif command == 'delete':
        records = delete(records)
    elif command == 'exit':
        save(init_money, records)
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')                                                     