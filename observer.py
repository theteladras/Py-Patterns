def Observer():
    listeners = []

    class PubSub(object):

        @staticmethod
        def subscribe(listener):
            listeners.append(listener)

            def unsubscribe():
                listeners.remove(listener)

            return unsubscribe

        @staticmethod
        def publish(event):
            for listener in listeners:
                listener(event)

    return PubSub


if __name__ == '__main__':
    ACT = Observer()

    unsubscribe1 = ACT.subscribe(lambda x: print(x))
    unsubscribe2 = ACT.subscribe(lambda x: print(x))

    unsubscribe1()

    ACT.publish("...da nije mozda...")
