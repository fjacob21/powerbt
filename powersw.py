import requests

class PowerSw(object):

    def __init__(self, server, port=8888):
        self._server = server
        self._port = port
        self._url = 'http://{0}:{1}/'.format(self._server, self._port)
    
    def reboot(self):
        requests.get(self._url + 'reboot')

    def poweroff(self):
        requests.get(self._url + 'poweroff')