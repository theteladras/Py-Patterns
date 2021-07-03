class Visitor(object):
    @staticmethod
    def visit(to_visit, cb, skip_keys=[]):
        accumulator = 0
        for x in to_visit:
            if x not in skip_keys:
                accumulator = cb(accumulator, to_visit[x])
        return accumulator


if __name__ == '__main__':
    def cb(accumulator, new):
        return accumulator + new

    fruits = Visitor.visit({
        "apples": 5,
        "pinaples": 3,
        "bananas": 1,
        "tomatos": 2,
        "watermelon": 3
    }, cb, ["watermelon"])

    print(fruits)
