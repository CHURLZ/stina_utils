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
