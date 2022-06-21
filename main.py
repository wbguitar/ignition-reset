import traceback

import ignition
import json
import logging
import logging.config
import time
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # adding config file param
    parser.add_argument('-c', default='config.json', help='Please provide a *.json config path', type=str)

    args_list = sys.argv[1:]
    args = parser.parse_args(args_list)
    config_file = args.c
    with open(config_file) as f:
        config = json.load(f)

    logging.config.fileConfig('logging.conf')
    logging.info("Server started...")
    try:
        while True:
            logging.debug("Rerun")
            ignition.reset_trial(config)
            time.sleep(config.get('polling', 10))
    except KeyboardInterrupt:
        pass
    except:
        logging.error(traceback.format_exc())

    logging.info("Server closing...")
