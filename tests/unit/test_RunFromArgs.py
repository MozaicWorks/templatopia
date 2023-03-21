from dataclasses import dataclass

import pytest

from templatopia.RunFromArgs import RunFromArgs


@dataclass
class Args:
    map:str
    map_from:str

class TestRunFromArgs:
    def test_run(self):
        with pytest.raises(FileNotFoundError):
            args = Args(
                    map = "",
                    map_from = ""
                    )
            RunFromArgs(args).run()
