import pytest

def read_properties_file():
    properties_dict = {}
    with open('python-auto-test/properties/properties.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                key_value = line.split("=")
                properties_dict[key_value[0].strip()] = key_value[1].strip()
    return properties_dict

def test_db_url():
    properties_dict = read_properties_file()
    assert properties_dict.get("spring.datasource.url") == "jdbc:mysql://localhost:3306/mydb"
