from factory import Factory


class Singleton(object):
    __memory = None

    def __init__(self) -> None:
        self.__memory = Factory().initDB("list")

    def get_memory(self):
        return self.__memory


if __name__ == '__main__':
    MEMORY = Singleton().get_memory()

    MEMORY.set("Jason")

    print(MEMORY.get_all())

    MEMORY_2 = Singleton().get_memory()

    print(MEMORY.get_all())
