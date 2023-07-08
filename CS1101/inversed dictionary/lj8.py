import json

# reading the data from the input file
with open('inputfile.txt', 'r') as file:
    data = file.read()
    # reconstructing the data as a dictionary
    d = json.loads(data)


def invert_dict(d):
     inverse = dict() 
     for key, val in d.items():
          for item in val: 
                if item not in inverse:
                    inverse[item] = [key]
                else:
                    inverse[item].append(key)
     return inverse

# writing the inverted dictionary in the output file
with open('outputfile.txt', 'w') as output_file:
     output_file.write(str(invert_dict(d)))
