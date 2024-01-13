from __future__ import annotations

from pytest import fixture, mark

count_1 = 0
count_2 = 0


@fixture(scope="class")
def _fixture_1():
    global count_1
    count_1 += 1


@fixture()
def _fixture_2(_fixture_1: None):
    global count_2
    count_2 += 1


@mark.usefixtures("_fixture_2")
class Test:
    @staticmethod
    def test_one():
        assert count_1 == 1
        assert count_2 == 1

    @staticmethod
    def test_two():
        assert count_1 == 1
        assert count_2 == 2
