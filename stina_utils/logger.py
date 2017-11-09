import os
import json
import logging.config
import logging

def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    global log
    logging.info('Logger loaded.')


if 'log' not in globals():
  setup_logging()
else:
  logging.info('Logger reloaded.')
