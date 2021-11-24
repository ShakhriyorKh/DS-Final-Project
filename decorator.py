from interface import *


#decorator used for functional decomposition. It sorts data in No-SQL using BST
def binary_tree(func):
    def wrapped_function():
        func()

        class Node:
            def __init__(self, data):
              self.left = None
              self.right = None
              self.data = data
              self.node = {
                  '_id': data['_id'],
                  'left_child': None,
                  'right_child': None,
                  'data': data['data']
              }

            def insert(self, data):
                if self.data["data"]["name"]:
                    if data["data"]["name"] < self.data["data"]["name"]:
                        if self.left is None:
                            self.node["left_child"] = data['_id']
                            self.left = Node(data)

                        else:
                            self.left.insert(data)

                    elif data["data"]["name"] > self.data["data"]["name"]:
                        if self.right is None:
                            self.node["right_child"]= data['_id']
                            self.right = Node(data)
                        else:
                            self.right.insert(data)

                else:
                    self.data = data

            def SaveTree(self, my_list=[]):
                if self.left:
                    self.left.SaveTree(my_list)
                my_list.append(self.node)
                if self.right:
                    self.right.SaveTree(my_list)

                return my_list


        # copying data from db
        data_from_db = []
        for document in collection.find():
            data_from_db.append(document)

        # middle = len(data_from_db)//2
        root = Node(data_from_db[0])

        # creating binary tree
        for document in data_from_db:
            root.insert(document)
        db_copy_sorted = root.SaveTree()

        # deleting data from db
        collection.delete_many({})

        # recording new sorted values
        for record in db_copy_sorted:
            collection.insert_one(record)

    return wrapped_function

def binary_tree_sort(func):
    def wrapped_function():
        func()

        class Node:
            def __init__(self, data):
              self.left = None
              self.right = None
              self.data = data

            def insert(self, data):
                if self.data["data"]["name"]:
                    if data["data"]["name"] < self.data["data"]["name"]:
                        if self.left is None:
                            self.left = Node(data)

                        else:
                            self.left.insert(data)

                    elif data["data"]["name"] > self.data["data"]["name"]:
                        if self.right is None:
                            self.right = Node(data)
                        else:
                            self.right.insert(data)

                else:
                    self.data = data

            def SaveTree(self, my_list=[]):
                if self.left:
                    self.left.SaveTree(my_list)
                my_list.append(self.data)
                if self.right:
                    self.right.SaveTree(my_list)

                return my_list


        # copying data from db
        data_from_db = []
        for document in collection.find():
            data_from_db.append(document)

        root = Node(data_from_db[0])

        # creating binary tree
        for document in data_from_db:
            root.insert(document)
        db_copy_sorted = root.SaveTree()

        # deleting data from db
        collection.delete_many({})

        # recording new sorted values
        for record in db_copy_sorted:
            collection.insert_one(record)

    return wrapped_function

def trees_survived_decorator(func):
    def wrapped_func():
        func()
        from random import randint
        from datetime import datetime
        sum = 0
        my_collection = collection.find({}, {'data.trees': 1})
        for i in my_collection:
            sum += i['data']['trees']
        survived = randint(sum//2, sum)
        record_time = datetime.now().strftime("%d/%m/%Y - %H:%M")
        obj = {
            'trees_took_root': survived,
            'record_time': record_time
        }
        collection_2.insert_one(obj)

    return wrapped_func

def funds_transferred_decorator(func):
    def wrapped_func():
        func()
        from datetime import datetime
        sum = 0
        my_collection = collection.find({}, {'data.remnant': 1})
        for i in my_collection:
            sum += i['data']['remnant']
        water_supply = sum * 0.4
        medical_treatment = sum * 0.4
        home_repairs = sum * 0.2
        record_time = datetime.now().strftime("%d/%m/%Y - %H:%M")

        obj = {
            'total_remnant': sum,
            'water_supply': water_supply,
            'medical_treatment': medical_treatment,
            'home_repairs': home_repairs,
            'record_time': record_time
        }
        collection_3.insert_one(obj)

    return wrapped_func
