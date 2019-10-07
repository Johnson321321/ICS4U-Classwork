import evaluation_prep as ep
def test_cal_sum():
    assert ep.cal_sum(1,2) == 3

def test_add_list():
    assert ep.cal_list_sum([]) == 0
    assert ep.cal_list_sum([1,2,3]) == 6
    assert ep.cal_list_sum([1,1,1]) == 3

def test_count_occurances():
    assert ep.count_occurances([]) == {}
    words = ['mer', 'mer','ner']
    expected = {'mer': 2, 'ner': 1}
    result = ep.count_occurances(words)
    assert result == expected

    words = ['mer', 'ner', 'mer', 'ner']
    expected = {'mer': 2, 'ner':2}
    result = ep.count_occurances(words)
    assert result == expected


