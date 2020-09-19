import pytest

from atcoder.dsu import DSU


@pytest.fixture
def dsu():
    return DSU(5)


class TestDsu:

    def test_initial_status(self, dsu):
        '''
        An initialized dsu object is expected to be independent of all
        vertices.

        GIVEN an initialized dsu object
        WHEN before executing dsu.merge(vertex a, vertex b)
        THEN all the vertices are independent
        '''

        pair_of_vertices = self._generate_pair_of_vertices()

        for first_vertex, second_vertex in pair_of_vertices:
            is_same = dsu.same(first_vertex, second_vertex)
            assert not is_same

        for index in range(5):
            assert dsu.size(index) == 1
            assert dsu.leader(index) == index

        assert dsu.groups() == [[0], [1], [2], [3], [4]]

    def _generate_pair_of_vertices(self):
        from itertools import combinations

        return list(combinations(range(5), 2))

    def test_merge(self, dsu):
        '''
        dsu.merge(vertex a, vertex b) is expected to be in the same group.

        GIVEN an initialized dsu object
        WHEN vertex 0 and 1 are merged
        THEN vertex 0 and 1 are the same group.
        '''

        is_same = dsu.same(0, 1)
        assert not is_same

        dsu.merge(0, 1)
        is_same = dsu.same(0, 1)
        assert is_same

    def test_merge_elements_of_same_group(self, dsu):
        '''
        merge elements of the same group.

        GIVEN an initialized dsu object
        WHEN merge vertex 0 and 1 twice
        THEN vertex 0 and 1 are the same group. Their size is 2.
        '''

        is_same = dsu.same(0, 1)
        assert not is_same

        for _ in range(2):
            dsu.merge(0, 1)
            is_same = dsu.same(0, 1)
            assert is_same
            assert dsu.size(0) == 2
            assert dsu.size(1) == 2

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

    def test_leader(self, dsu):
        '''
        dsu.leader(vertex a) is expected to return the representative of the
        connected component that contains the vertex a.

        GIVEN an initialized dsu object
        WHEN vertex 0, 1 and 2 are merged
        THEN vertex 1 and 2 belong to any of the vertices 0-2.
        '''

        dsu.merge(0, 1)
        dsu.merge(0, 2)

        assert dsu.leader(1) in [0, 1, 2]
        assert dsu.leader(2) in [0, 1, 2]
        assert dsu.leader(1) == dsu.leader(2)
        assert dsu.leader(3) not in [0, 1, 2]
        assert dsu.leader(4) not in [0, 1, 2]

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

    @pytest.mark.parametrize((
        'vertex_a', 'vertex_b'
        ), [
        (-2, 4),
        (-1, 4),
        (0, 5),
        (0, 6),
        (-1, 5),
        (-1, 6),
    ])
    def test_merge_failed_if_invalid_input_is_given(self, dsu,
                                                    vertex_a, vertex_b):
        '''
        dsu.merge(vertex a, vertex b) is expected to be raised an
        AssertionError if an invalid input is given.

        GIVEN an initialized dsu object
        WHEN an out-of-range index is given
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            dsu.merge(vertex_a, vertex_b)

    @pytest.mark.parametrize((
        'vertex_a', 'vertex_b'
        ), [
        (-2, 4),
        (-1, 4),
        (0, 5),
        (0, 6),
        (-1, 5),
        (-1, 6),
    ])
    def test_same_failed_if_invalid_input_is_given(self, dsu,
                                                   vertex_a, vertex_b):
        '''
        dsu.same(vertex a, vertex b) is expected to be raised an AssertionError
        if an invalid input is given.

        GIVEN an initialized dsu object
        WHEN an out-of-range index is given
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            dsu.same(vertex_a, vertex_b)

    @pytest.mark.parametrize((
        'vertex_a'
        ), [
        -2,
        -1,
        5,
        6,
    ])
    def test_leader_failed_if_invalid_input_is_given(self, dsu, vertex_a):
        '''
        dsu.leader(vertex a) is expected to be raised an AssertionError if an
        invalid input is given.

        GIVEN an initialized dsu object
        WHEN an out-of-range index is given
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            dsu.leader(vertex_a)

    @pytest.mark.parametrize((
        'vertex_a'
        ), [
        -2,
        -1,
        5,
        6,
    ])
    def test_size_failed_if_invalid_input_is_given(self, dsu, vertex_a):
        '''
        dsu.size(vertex a) is expected to be raised an AssertionError if an
        invalid input is given.

        GIVEN an initialized dsu object
        WHEN an out-of-range index is given
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            dsu.size(vertex_a)
