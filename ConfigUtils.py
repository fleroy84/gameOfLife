

class ConfigUtil(object) :
    
    @staticmethod
    def loadPattern():
        pattern = open("patterns/gosper.txt", "r")
        data = pattern.read()
        print(data)
        pattern.close()
        return data