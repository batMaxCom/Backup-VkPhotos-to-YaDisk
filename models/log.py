def logger(some_function):
    def new_function(*args,**kwargs):
        result = some_function(*args, **kwargs)
        with open('LOGS/LOG.json', "a", encoding='utf-8') as f:
            f.write(str(result) + f'\n')
        f.close()
        return result
    return new_function

