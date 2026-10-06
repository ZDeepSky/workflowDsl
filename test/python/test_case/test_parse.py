
import pytest
import dispatch.dsl_generator.convert_dsl as convert_dsl


class TestParse:
    def test_parse_success(self):
        with open("test_case/test_syncfunc.dsl", "r") as file:
            dsl_text = file.read()
        model = convert_dsl.parse_dsl(dsl_text)
        assert model is not None
        assert model["workflows"] is not None
        assert model["workflows"][0]["name"] == "synctrans"
        assert model["workflows"][0]["actions"] is not None
        assert model["workflows"][0]["actions"][0]["name"] == "action1"
        assert model["workflows"][0]["actions"][1]["name"] == "action2"
        assert model["workflows"][0]["actions"][2]["name"] == "procedure01"


