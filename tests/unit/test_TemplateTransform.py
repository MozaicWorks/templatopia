import io
from parameterized import parameterized

class TestTemplateTransform:
    @parameterized.expand([
           ("one no mapping", "Hello {{first_name}}",  [{"first_name": "John"}], "Hello John"),
       ])
    def test_transform_one(self, name, template, table, expected):
        template="Hello {{first_name}}"
        table = [{"first_name": "John"}]
        expected = "Hello John"

        transformed = transform(template, table)

        assert transformed == expected 


def transform(template, table):
    import pystache
    return pystache.render(template, table[0])


