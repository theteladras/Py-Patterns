class Factory(object):
    class Dict(object):
        __memory = None

        def __init__(self):
            self.__memory = {}

        def get(self, id):
            return self.__memory[id]

        def get_all(self):
            return self.__memory

        def set(self, record):
            record_key = record["id"].lower()
            self.__memory[record_key] = record

        def remove(self, id):
            del self.__memory[id]

    class List(object):
        __memory = None

        def __init__(self):
            self.__memory = []

        def get(self, id):
            item_index = self.__memory.index(id)
            return self.__memory[item_index]

        def get_all(self):
            return self.__memory

        def set(self, id):
            if id in self.__memory:
                return
            self.__memory.append(id)

        def remove(self, id):
            item_index = self.__memory.index(id)
            if not item_index:
                return
            del self.__memory[item_index]

    def initDB(self, target):
        if target == 'list':
            return self.List()
        if target == 'dict':
            return self.Dict()
        raise Exception("invalid db requested")


if __name__ == '__main__':
    DICT_DB = Factory().initDB("dict")

    DICT_DB.set({
        "id": "Seat",
        "model": "Toledo",
        "hp": 120,
        "year": 2015
    })
    DICT_DB.set({
        "id": "Opel",
        "model": "Corsa",
        "hp": 77,
        "year": 2001
    })

    print(DICT_DB.get("opel"))

    LIST_DB = Factory().initDB("list")

    LIST_DB.set("Neptun")
    LIST_DB.set("Uranus")
    LIST_DB.set("Alfa")
    print(LIST_DB.get_all())

    LIST_DB.remove("Alfa")
    print(LIST_DB.get_all())
