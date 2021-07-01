result = set()

with open('./Untitled', 'r') as source:
    for row in source.readlines():
        result.add(row.strip())

result = ''.join(list(result))

with open('./output', 'w+') as output:
    output.write(result)