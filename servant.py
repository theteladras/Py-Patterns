class Event:

    def __init__(self, type, name, date):
        self.type = type
        self.name = name
        self.date = date

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

    def getType(self):
        return self.type


class User:
    events = []

    def __init__(self, name):
        self.name = name

    def getEventsByDate(self):
        return [x.date for x in self.events]

    def schedule(self, event):
        self.events.append(event)


def serveSchedule(user, event):
    user.schedule(event)

    return user.getEventsByDate()


if __name__ == '__main__':
    gosn = User('Gosn')

    event = Event('sport', 'tennis', '2021-07-03T21:16:28.343Z')

    scheduled = serveSchedule(gosn, event)

    print(scheduled)
