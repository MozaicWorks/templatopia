from dataclasses import dataclass

from TransformedRow import TransformedRow

from Template import Template


@dataclass
class RowTemplate:
    nameTemplate: Template
    contentTemplate: Template

    def render(self, values) -> TransformedRow:
        return TransformedRow(
                self.nameTemplate.render(values),
                self.contentTemplate.render(values)
                )
