def pytest_addoption(parser):
    parser.addoption('--base-url', action='store', default='http://localhost:8080', help='Base URL for the API tests')
