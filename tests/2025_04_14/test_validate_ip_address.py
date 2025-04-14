from src.practice_2025_04_14.validate_ip_address import validate_ip_address

def test_valid_ip():
    assert validate_ip_address("192.168.1.1") is True

def test_out_of_range():
    assert validate_ip_address("256.100.50.0") is False

def test_leading_zero():
    assert validate_ip_address("192.168.01.1") is False

def test_not_four_parts():
    assert validate_ip_address("192.168.1") is False

def test_non_numeric():
    assert validate_ip_address("abc.def.ghi.jkl") is False
