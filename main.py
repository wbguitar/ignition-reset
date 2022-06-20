import ignition

config = {
    'webdriver': 'edge',
    'gateway': 'http://localhost:80',
    'auth': {
        'username': 'admin',
        'password': 'admin'
    }
}

if __name__ == '__main__':
    ignition.run(config)
