
from types import SimpleNamespace
import collections


class Resident():
    resident = {}

    def __init__(self, data):
        self.resident = SimpleNamespace(**data)
        # self.res = data

    def add_title(self):
        self.resident.name = 'Sir ' + self.resident.name
        # self.res['name'] = 'SIr' + self.res['name']
        # print(self.resident)
        return collections.OrderedDict(self.resident.__dict__)
