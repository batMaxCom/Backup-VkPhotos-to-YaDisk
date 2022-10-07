import json


def logger(some_function):
    def new_function(*args, **kwargs):
        result = some_function(*args, **kwargs)
        with open('LOGS/LOG.json') as f:
            data = json.load(f)

        data += result

        with open('LOGS/LOG.json', 'w') as f:
            json.dump(data, f)

        return result

    return new_function
