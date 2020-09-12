import os
import sys

# Add path.
# See:
# https://www.magata.net/memo/index.php?pytest%C6%FE%CC%E7#y2046859
path = os.path.dirname(os.path.abspath(__file__)) + '/../atcoder/'
sys.path.append(os.path.abspath(path))
