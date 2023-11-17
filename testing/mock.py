
def fetch_data(query):
    # A complicated query to a remote database
    return []

def process_data():
    res = fetch_data('SELECT * FROM some_table')

    data = []
    for row in res:
        row['field1'] = row['field1'].upper()
        row['field2'] = int(row['field2'])
        data.append(row)

    return data


