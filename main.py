import ignition
import json

if __name__ == '__main__':
    config = ''
    with open('config.json') as f:
        config = json.load(f)
    ignition.run(config)
