import re
from os import path

while True:
    file_path = input('Please enter the path of the G-Code file: ')
    if (path.exists(file_path)):
        break

while True:
    axis_mirror = input('Please select the axis mirror (X, Y): ')
    if (axis_mirror == 'X' or axis_mirror == 'Y'):
        break

input_file = open(file_path, "r")

axis_list = []
content = []
for line in input_file:
  string_list = line.split()
  for string in string_list:
      if string.startswith(axis_mirror):
          axis_list.append(float(string[1:]))
          break
  content.append(' '.join(string_list))

axis_min = min(axis_list)
axis_max = max(axis_list)

def remap(matchstring):
    return axis_mirror + str((((float(matchstring.group(0)[1:]) - axis_min) * (axis_min - axis_max)) / (axis_max - axis_min)) + axis_max)

file_name, file_extension = path.splitext(file_path)
output_file = open(file_name + "_output" + file_extension, "w")

new_content = []
for line in content:
  new_content.append(re.sub('X[+-]?([0-9]*[.])?[0-9]+', remap, line))

output_file.write('\n'.join(new_content))

input_file.close()
output_file.close()
