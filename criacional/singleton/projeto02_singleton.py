
class SanityCheck:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanityCheck.__instance:
            SanityCheck.__instance = super(SanityCheck, cls).__new__(cls, *args, **kwargs)
        return SanityCheck.__instance

    def __init__(self):
        self.__servers = []

    def check_server(self, server):
        print(f'Checking {self.__servers[server]}')

    def add_server(self):
        self.__servers.append('Server 01')
        self.__servers.append('Server 02')
        self.__servers.append('Server 03')
        self.__servers.append('Server 04')
        self.__servers.append('Server 05')
    
    def change_server(self):
        self.__servers.pop()
        self.__servers.append('Server 06')

srv1 = SanityCheck()
srv2 = SanityCheck()

srv1.add_server()
print('Sanity Check cronogram A')
for s in range(5):
    srv1.check_server(s)

print("\n")

srv2.change_server()
print('Sanity Check cronogram B')
for s in range(5):
    srv2.check_server(s)