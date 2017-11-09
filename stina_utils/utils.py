import os

def get_env_var(var, optional=False):
    try:
        valid_var = os.getenv(var)
        if not valid_var:
            raise Exception
        return valid_var
    except:
        print('Environment variable not found: {}'.format(var))
        raise

dict_without_key = lambda d, x: {i:d[i] for i in d if i != x}

def split_dict(data, key):
    return data[key], dict_without_key(data, key)
