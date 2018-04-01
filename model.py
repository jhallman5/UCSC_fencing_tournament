import sys
import csv
from linked_list import Node, Linked_List

def create_linked_list():
    ''' Creates a sorted linked list from a CSV file. '''
    with open(sys.argv[1]) as csv_file:
        fencer_list = Linked_List()
        reader = csv.reader(csv_file, delimiter='\t')
        for row in reader:
            fencer = {
            'last_name': row[0].split(',')[0],
            'first_name': row[0].split(',')[1],
            'team': row[0].split(',')[2],
            'rank':row[0].split(',')[3]
            }
            fencer_list.insert(fencer)
        return fencer_list
