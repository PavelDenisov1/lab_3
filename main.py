import yaml
from package.file_reader import file_reader
from package.sort import selection_sort

object = file_reader('output.txt')
data = object.get_data()
selection_sort(data)


ser = yaml.dump(object)
with open('sample.yaml', 'w') as f:
    f.write(ser)
f.close()

with open('sample.yaml', 'r') as f:
    ser_2 = f.read()
f.close()

obj_2 = yaml.load(ser_2, Loader=yaml.Loader)
data_2 = obj_2.get_data()

f = open('sorted.txt', 'w', encoding='utf-8')
for i in data_2:
    f.write(str(i) + "\n")
f.close()