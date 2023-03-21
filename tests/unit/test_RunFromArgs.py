from dataclasses import dataclass
from pathlib import Path

import pytest

from templatopia.RunFromArgs import RunFromArgs


@dataclass
class Args:
    map:str
    from_csv:str
    name_template:str
    template:str
    common_value:str
    verbose:bool
    common_values_from:str="common-values.json"
    map_from:str="map.json"
    template_path:str="./template/"
    to_path:str="out/"

class TestRunFromArgs:
    @pytest.fixture
    def test_run(self, tmp_path):
        args = Args(
                map = None,
                from_csv = "in/list.csv",
                name_template="{{first_name}}{{last_name}}",
                template = "template.svg",
                common_value = None,
                to_path = str(tmp_path),
                verbose = False
                )
        RunFromArgs(args).run()

        assert Path(args.to_path, "Jane-Doe.svg").exists()
        assert Path(args.to_path, "John-Doe.svg").exists()
