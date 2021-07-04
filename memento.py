class Go():
    state = (None, None)
    saved_states = []

    def move(self, x, y):
        self.state = (x, y)

    def save(self):
        self.saved_states.append(self.Memento(self.state))

    def getSaves(self):
        saved_states = self.saved_states
        print(saved_states)
        return saved_states

    def undo(self, memento):
        state_to_undo = memento.getSavedState()
        self.state = state_to_undo
        self.saved_states.remove(memento)

    class Memento():
        __state__ = (None, None)

        def __init__(self, state):
            self.__state__ = state

        def getSavedState(self):
            return self.__state__


if __name__ == '__main__':
    baduk = Go()

    baduk.move(4, 4)
    baduk.save()
    baduk.move(15, 15)
    baduk.save()

    saves = baduk.getSaves()

    baduk.undo(saves[0])

    baduk.getSaves()
