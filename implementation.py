import os
from interface import *
from decorator import (
    binary_tree,
    binary_tree_sort,
    trees_survived_decorator,
    funds_transferred_decorator)


# function for clearing console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# function for recording transactions
@binary_tree_sort
@binary_tree
@trees_survived_decorator
@funds_transferred_decorator
def plantTree():
    clearConsole()
    print('-' * 15)
    name = input("Your Full Name: ")
    address = input("City of residence: ")
    funds = int(input("How much do you want to donate (1 tree = 15$):"))
    clearConsole()
    trees = funds // 15
    remnant = funds % 15
    print('Remnant funds will be allocated to Social Fund')
    print("*" * 10, f"\n\nTotal number of trees: {trees}\nRemnant fund: {remnant}$\nTotal: {funds}$\n")
    print("*" * 10)
    confirmation = input("Confirm transaction? y(yes) / N(no): ")
    if confirmation == "y":
        clearConsole()
        filter = {"_id": name}
        if not collection.find_one(filter):
            collection.insert_one(
                {
                    "_id": name,
                    "data": {"name": name,
                             "address": address,
                             "funds": funds,
                             "trees": trees,
                             "remnant": remnant,
                             },
                }
            )
        else:
            print()
        print("Funds have been successfully transferred.\nThanks for your contribution to Green Future of generations!")
        print('-' * 15)

    elif confirmation == "N":
        clearConsole()
        pass
    else:
        print("Invalid input")


# function for printing list of transactions
def listOfDonors():
    # function for printing the number of trees survived
    clearConsole()
    print('-' * 15)
    my_collection = collection.find().sort("data.funds", -1)
    for object in my_collection:
        data = object['data']
        print(f"[Name: {data['name']} - Funds {data['funds']}$ - Trees: {data['trees']} - Address: {data['address']}]")
    print('-' * 15)


def treesSurvived():
    clearConsole()
    print('-' * 15)
    print("Number of trees that survived harsh climate of Aral Kum:\n")
    data = collection_2.find().sort('record_time', -1)
    for i in data:
        print(f"[Trees took root: {i['trees_took_root']} -|- Record time: {i['record_time']}]")
    print('-' * 15)


def fundsTransferred():
    clearConsole()
    print('-' * 15)
    print("Surplus funds were invested into three public sectors:\n1. Improving access to drinking water\n2. Medical checkup and treatment of the population\n3. Repair of houses of the local population")
    data = collection_3.find().sort('record_time', -1)
    for i in data:
        print('')
        print(f"Record time: {i['record_time']} -|- Total surplus funds: {i['total_remnant']}$")
        print(f"[Medical sector: {i['medical_treatment']}$ -|- Water supply: {i['water_supply']}$ -|- Infrastructure maintaince: {i['home_repairs']}$]")
        print('')
    print('-' * 15)



