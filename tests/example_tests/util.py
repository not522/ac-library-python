from pathlib import Path
from subprocess import check_output
import sys


def run(source, stdin):
    source_path = Path(__file__).parent.parent.parent / 'example' / source
    return check_output((sys.executable, source_path), stdin=stdin)
