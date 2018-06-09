import json


class Data(object):
    def __init__(self):
        self.data = []
        self.status = 0
        self.is_end_work = 0
        self.name_file = 'data_values.json'

    def write_file(self, values):
        with open(self.name_file, 'w') as f:
            f.write(json.dumps(values))

    def get_values(self):
        values = dict()
        with open(self.name_file, 'r') as f:
            values = json.loads(f.readline())
        return values