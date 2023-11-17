from testing.mock import process_data

def test_process_data(mocker):
    import testing
    mocker.patch('testing.mock.fetch_data', return_value=[
        { 'field1': 'r', 'field2': '3', 'field3': 'u' }
    ])

    spy = mocker.spy(testing.mock, 'fetch_data')

    assert process_data() == [{ 'field1': 'R', 'field2': 3, 'field3': 'u' }]
    spy.assert_called_once_with('SELECT * FROM some_table')
