from testing.basic import parser

def complex(data):
    return [x+x for x in data.split(',')]

def complex_1(data):
    parts = []
    rows = data.split(',')
    for row in rows:
        fields = []
        for field in row.split('|'):
            if field.isnumeric():
                fields.append(int(field))
            else:
                fields.append(field+field)

        parts.append(fields)

    return parts

def complex_2(data):
    return [parser(x, '|', lambda val: int(val) if val.isnumeric() else val+val) for x in parser(data)]
