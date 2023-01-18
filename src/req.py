class GetRequirements ():
    def __init__(self,file):
        self.file=file
        for line in self.file:
            var = line.split('=')[0]
            value = line.split('=')[1]
            if var == "vers":
                self.version = value


if __name__ == '__main__':
    with open ('vers.txt') as file:
        print(GetRequirements(file).version)
