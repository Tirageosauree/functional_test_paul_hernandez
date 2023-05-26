from exercice2 import StringAnalyzer

def test_string_analyzer_vowels():
    sa = StringAnalyzer("hello")
    assert sa.count_vowels() == 2

def test_string_analyzer_consonants():
    sa = StringAnalyzer("hello")
    assert sa.count_consonants() == 3

def test_string_analyzer_digits():
    sa = StringAnalyzer("1234hello5678")
    assert sa.count_digits() == 8

def test_string_analyzer_words():
    sa = StringAnalyzer("hello world how are you")
    assert sa.count_words() == 5

def test_string_analyzer_lines():
    sa = StringAnalyzer("hello\nworld\nhow\nare\nyou")
    assert sa.count_lines() == 5
