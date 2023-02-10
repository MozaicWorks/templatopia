import io

class TestTemplateTransform:

    def test_transform(self):
        template="Hello {{first_name}} {{last_name}}"
        table = [
                {"firstName": "John", "lastName": "Doe"},
                {"firstName": "Jane", "lastName": "Dow"}
                ]

        mapping = {"firstName":"first_name", "lastName":"last_name"}
        writer = io.StringIO("")
        expected = """Hello John Doe
        Hello Jane Doe"""

        templateTransform = TemplateTransform(template, table, mapping, writer)

        templateTransform.transform()

        assert writer.getvalue() == expected 


class TemplateTransform:
    def __init__(self, template, table, mapping, writer):
        pass

    def transform(self):
        pass
