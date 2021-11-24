# connecting to MongoDB
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://admin:admin@mycluster.b2pf9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['ds_project']
collection = db['transactions']
collection_2 = db['trees_survived']
collection_3 = db['public_fund']


if __name__ == "__main__":
    import msvcrt as m
    import implementation

    print("Welcome to the Save Aral Program")
    print("Press 'Enter' to continue...")
    m.getch()
    implementation.clearConsole()

    while True:
        print("""1 - plant tree
2 - list of donors
3 - trees took root
4 - public sector
        
0 - exit""")
        option = int(input(">>> "))
        if option == 1:
            implementation.plantTree()

        elif option == 2:
            implementation.listOfDonors()

        elif option == 3:
            implementation.treesSurvived()

        elif option == 4:
            implementation.fundsTransferred()

        elif option == 0:
            print("Have a good day!")
            break

        else:
            print("Not existing option")







