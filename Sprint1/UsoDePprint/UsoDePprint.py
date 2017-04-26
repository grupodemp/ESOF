import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'Flufly'}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
fileObj = open('myCats.py', 'r')
fileContent = fileObj.read()
fileObj.close()
print(fileContent)
