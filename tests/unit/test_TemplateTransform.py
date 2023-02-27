from parameterized import parameterized
from templatopia.transformer import Transformer


class TestTemplateTransform:
    @parameterized.expand([
           ("no mapping", "Hello {{first_name}}",  {"first_name": "John"}, "Hello John"),
       ])
    def test_transform_no_mapping(self, name, template, values, expected):
        theTransformer = Transformer(values)

        transformed = theTransformer.transform(template)

        assert transformed == expected

    @parameterized.expand([
        ("one mapping", "Hello {{firstName}}",  {"first_name": "John"}, {"first_name": "firstName"}, "Hello John"),
        ("two mappings", "{{firstName}}-{{lastName}}.svg",  {"first_name": "John", "last_name":"Doe"}, {"first_name": "firstName", "last_name": "lastName"}, "John-Doe.svg"),
       ])
    def test_transform_mapping(self, name, template, values, mapping, expected):
        theTransformer = Transformer(values, mapping)

        transformed = theTransformer.transform(template)

        assert transformed == expected

    @parameterized.expand([
        ("template value not found", "Hello {{firstName}}",  {'name': "John Doe"}, {}, "Hello "),
        ("mapping not found", "Hello {{firstName}}",  {'first_name': "John", "last_name": "Doe", "user_email": "john@doe.com"}, {"first_name":"firstName", "last_name":"lastName"}, "Hello John"),
       ])
    def test_edge_cases(self, name, template, values, mapping, expected):
        theTransformer = Transformer(values, mapping)

        transformed = theTransformer.transform(template)

        assert transformed == expected
