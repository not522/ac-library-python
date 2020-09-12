import pytest

from atcoder.dsu import DSU


@pytest.fixture
def dsu():
    return DSU(5)


class TestDsu(object):

    def test_merge(self, dsu):
        '''
        dsu.merge(vertex a, vertex b) is expected to be in the same group.

        GIVEN an initialized dsu object
        WHEN vertex 0 and 1 are merged
        THEN vertex 0 and 1 are the same group.
        '''

        is_same = dsu.same(0, 1)
        assert is_same is False

        dsu.merge(0, 1)
        is_same = dsu.same(0, 1)
        assert is_same is True

    def test_size(self, dsu):
        '''
        dsu.size(vertex a) is expected to get size of vertex a.

        GIVEN an initialized dsu object
        WHEN vertex 0, 1 and 2 are merged
        THEN size of vertex 0 is 3.
        '''

        dsu.merge(0, 1)
        dsu.merge(0, 2)
        assert dsu.size(0) == 3

        is_same = dsu.same(0, 3)
        assert is_same is False

        is_same = dsu.same(0, 4)
        assert is_same is False

    def test_leader(self, dsu):
        '''
        dsu.leader(vertex a) is expected to return the representative of the
        connected component that contains the vertex a.

        GIVEN an initialized dsu object
        WHEN vertex 0, 1 and 2 are merged
        THEN vertex 1 and 2 belong to vertex 0.
        '''

        dsu.merge(0, 1)
        dsu.merge(0, 2)

        assert dsu.leader(1) == 0
        assert dsu.leader(2) == 0
        assert dsu.leader(3) != 0
        assert dsu.leader(4) != 0

    def test_groups(self, dsu):
        '''
        dsu.groups() is expected to return the list of the graph that divided
        into connected components.

        GIVEN an initialized dsu object
        WHEN vertex 0, 1 and 2 are merged
        THEN returns [[0, 1, 2], [3], [4]]
        '''

        dsu.merge(0, 1)
        dsu.merge(0, 2)

        assert dsu.groups() == [[0, 1, 2], [3], [4]]
