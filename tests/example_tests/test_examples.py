from pathlib import Path

import pytest

import util


class TestExamples:
    @pytest.mark.parametrize('problem_id, source', (
        ('A', 'dsu_practice.py'),
        ('B', 'fenwick_practice.py'),
        ('C', 'floor_sum_practice.py'),
        ('D', 'maxflow_practice.py'),
        ('E', 'mincostflow_practice.py'),
        ('F', 'convolution_practice.py'),
        ('F', 'convolution_practice_int.py'),
        ('G', 'scc_practice.py'),
        ('H', 'twosat_practice.py'),
        ('I', 'sa_practice.py'),
        ('J', 'segtree_practice.py'),
        ('J', 'segtree_practice_reversed.py'),
        ('K', 'lazysegtree_practice_k.py'),
        ('K', 'lazysegtree_practice_k_wo_modint.py'),
        ('L', 'lazysegtree_practice_l.py')))
    def test_examples(self, problem_id, source) -> None:
        input_path = (Path(__file__).parent / 'input')
        stdin_paths = list(input_path.glob(f'{problem_id}*_in.txt'))
        stdout_paths = list(input_path.glob(f'{problem_id}*_out.txt'))
        stdin_paths.sort()
        stdout_paths.sort()

        for stdin_path, stdout_path in zip(stdin_paths, stdout_paths):
            with open(stdin_path) as stdin:
                output = util.run(source, stdin).decode()

            with open(stdout_path) as stdout:
                assert output == stdout.read()
