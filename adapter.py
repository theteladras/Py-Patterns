from abc import ABC, abstractmethod
import json
import csv
import io


class Adapter(ABC):
    @abstractmethod
    def adapt(self, text):
        pass


class StringToJson(Adapter):
    originalContent = ""

    def adapt(self, text):
        self.originalContent = text
        return json.loads(text)


class CsvToJson(Adapter):
    originalContent = ""

    def adapt(self, text):
        self.originalContent = text
        reader = csv.DictReader(io.StringIO(text.strip()))
        return json.dumps(list(reader))


def work(text, adapter):
    content = adapter.adapt(text)
    print(content)


if __name__ == '__main__':
    content_1 = '[{"name" : "Luke", "surname" : "Skywalker", "gender" : "M"},{"Ben" : 1, "Solo" : 2, "gender" : "M"}]'

    work(content_1, StringToJson())

    content_2 = """
name,surname,gender
Anakin,Skywalker,M
Padme,Amidala,F
"""

    work(content_2, CsvToJson())
