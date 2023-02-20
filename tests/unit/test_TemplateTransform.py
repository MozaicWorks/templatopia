import io
from parameterized import parameterized
from templatopia.transformer import transform
from pytest import raises

class TestTemplateTransform:
    @parameterized.expand([
           ("zero items no mapping", "Hello {{first_name}}",  [], []),
           ("one item no mapping", "Hello {{first_name}}",  [{"first_name": "John"}], ["Hello John"]),
           ("two item no mapping", "Hello {{first_name}}",  [{"first_name": "John"}, {"first_name": "Jane"}], ["Hello John", "Hello Jane"]),
       ])
    def test_transform_no_mapping(self, name, template, table, expected):
        transformed = transform(template, table)

        assert transformed == expected 

    @parameterized.expand([
        ("zero items one mapping", "Hello {{firstName}}",  [], {"first_name":"firstName"}, []),
        ("one item one mapping", "Hello {{firstName}}",  [{"first_name": "John"}], {"first_name": "firstName"}, ["Hello John"]),
        ("two items one mapping", "Hello {{firstName}}",  [{"first_name": "John"}, {"first_name": "Jane"}], {"first_name": "firstName"}, ["Hello John", "Hello Jane"]),
        ("two items two mappings", "Hello {{firstName}} {{lastName}}",  [{"first_name": "John", "last_name":"Doe"}, {"first_name": "Jane", "last_name": "Dow"}], {"first_name": "firstName", "last_name": "lastName"}, ["Hello John Doe", "Hello Jane Dow"]),
        ("bug", "Hello {{firstName}} {{lastName}}",  [{"first_name": "John", "last_name":"Doe"}], {"first_name": "firstName", "last_name": "lastName"}, ["Hello John Doe"]),
       ])
    def test_transform_mapping(self, name, template, table, mapping, expected):
        transformed = transform(template, table, mapping)

        assert transformed == expected 

    def test_mapping(self):
        mappingArgs = ["firstName:first_name", "lastName:last_name"] 
        mapping = {item.split(":")[0]:item.split(":")[1] for item in mappingArgs}
        assert mapping["firstName"] == "first_name"
        assert mapping["lastName"] == "last_name"
 

    @parameterized.expand([
        ("template value not found", "Hello {{firstName}}",  [{'name': "John Doe"}], {}, ["Hello "]),
       ])
    def test_edge_cases(self, name, template, table, mapping, expected):
        transformed = transform(template, table, mapping)

        assert transformed == expected 
