from friday import is_anagram


def test_anagram():
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("listen", "silent") == True
    assert is_anagram("elbow", "below") == True
    assert is_anagram("elbows", "below") == False
    assert is_anagram("elbow", "below") == False
    assert is_anagram("a", "ab") == False
    assert is_anagram("ab", "a") == False
    assert is_anagram("ab", "ba") == True
    assert is_anagram("abc", "cba") == True
    assert is_anagram("abbc", "cba") == False
    assert is_anagram("abbc", "cbad") == False
    assert is_anagram("abbc", "cbac") == True
    assert is_anagram("abbc", "cbacd") == False
    assert is_anagram("abbc", "cbacd") == False


def test_anagram_empty():
    assert is_anagram("", "") == True
    assert is_anagram("", "a") == False
    assert is_anagram("a", "") == False
    assert is_anagram("", "ab") == False
    assert is_anagram("ab", "") == False
    assert is_anagram("", "abc") == False
    assert is_anagram("abc", "") == False
    assert is_anagram("", "abbc") == False
    assert is_anagram("abbc", "") == False
