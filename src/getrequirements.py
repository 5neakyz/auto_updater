import urllib.request

class GetRequirements ():
    def __init__(self,file):
        self.file=file
        self.reqs_dict = {}
        for line in self.file:
            line = line.replace('\n','')
            var = line.split('=')[0]
            value = line.split('=')[1]
            self.reqs_dict[var] = value
            
    def get_config_dict(self):
        return self.reqs_dict

if __name__ == '__main__':

    fileData = None
    with open ('src/vers.txt') as f:
        fileData = f.readlines()

    target_url = 'https://raw.githubusercontent.com/5neakyz/auto_updater/main/vers.txt'
    data = urllib.request.urlopen(target_url)
    data = data.readlines()
    temp = []
    for line in data:
        temp.append(line.decode())    
    print(temp)  
    print(data)
    print(GetRequirements(temp).get_config_dict())
