import tail_2_3

def test_getFilesFromArg_only_files():
    files = tail_2_3.getFilesFromArg(['pyton_script_file.py', 'a','b'])
    assert (files[0].name == 'a')
    assert (files[0].numberOfLines == 10)
    assert (files[1].name == 'b')
    assert (files[1].numberOfLines == 10)

def test_getFilesFromArg_files_and_number_of_lines():
    files = tail_2_3.getFilesFromArg(['pyton_script_file.py', 'a', '-2','b','-3'])
    assert (files[0].name == 'a')
    assert (files[0].numberOfLines == 2)
    assert (files[1].name == 'b')
    assert (files[1].numberOfLines == 3)

def test_getFilesFromArg_files_and_one_number_of_lines():
    files = tail_2_3.getFilesFromArg(['pyton_script_file.py', 'a', 'b','-3'])
    assert (files[0].name == 'a')
    assert (files[0].numberOfLines == 10)
    assert (files[1].name == 'b')
    assert (files[1].numberOfLines == 3)

def test_getIndex_list_less_than_number_of_lines():
    assert 0 == tail_2_3.getIndex([0,1,2,3],10)

def test_getIndex_list_equals_number_of_lines():
    assert 0 == tail_2_3.getIndex([0,1,2,3],4)    

def test_getIndex_list_bigger_than_number_of_lines():
    assert 3 == tail_2_3.getIndex([0,1,2,3],1)

