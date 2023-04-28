import pytest
from battlemaster.rules.tables.cluster_hits import cluster_hits_table


@pytest.fixture()
def cluster_hits():
    return cluster_hits_table()


def test_cluster_hits_table(cluster_hits):
    print(cluster_hits)
    a = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 12]
    b = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 18]
    c = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 13, 14, 15, 16, 16, 17, 17, 17, 18, 18, 24]
    d = [2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 20, 21, 21, 22, 23, 23, 24, 32]
    e = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40]

    assert(cluster_hits.get_sub_table(2) == a)
    assert(cluster_hits.get_sub_table(3) == a)
    assert(cluster_hits.get_sub_table(4) == b)
    assert(cluster_hits.get_sub_table(5) == c)
    assert(cluster_hits.get_sub_table(6) == c)
    assert(cluster_hits.get_sub_table(7) == c)
    assert(cluster_hits.get_sub_table(8) == c)
    assert(cluster_hits.get_sub_table(9) == d)
    assert(cluster_hits.get_sub_table(10) == d)
    assert(cluster_hits.get_sub_table(11) == e)
    assert(cluster_hits.get_sub_table(12) == e)
