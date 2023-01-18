import urllib.request

class GetRequirements ():
    def __init__(self,file):
        self.file=file
        for line in self.file:
            line = line.strip().replace(b'\n',b'').decode('utf-8')
            print(line)
            var = line.split('=')[0]
            value = line.split('=')[1]
            if var == "vers":
                self.version = value


if __name__ == '__main__':
    target_url = 'https://raw.githubusercontent.com/5neakyz/auto_updater/main/vers.txt'
    data = urllib.request.urlopen(target_url)
    print(GetRequirements(data).version)
