import pytest


@pytest.mark.parametrize("test_list, expected", [([2.8, 2.5, 0.7, 3.8, 2.7,
                                                   0.2, 2.9, 1.5, 0.8, 2.4, 2],
                                                  "hyperthyroidism"),
                                                 ([2.5, 1.1, 1.3, 2.7,
                                                   1.9, 2.6, 3.5, 1, 1.4],
                                                  "normal thyroid function"),
                                                 ([6.3, 6.7, 6.3,
                                                   7.6, 2.1, 6.9, 7.1,
                                                   4.1, 7.2, 3.5, 2.9],
                                                  "hypothyroidism"),
                                                 ([5], "hypothyroidism"),
                                                 ([0.9], "hyperthyroidism"),
                                                 ([2.9],
                                                  "normal thyroid function")
                                                 ])
def test_diagnose_tsh(test_list, expected):
    from tsh_data import diagnose_tsh
    result = diagnose_tsh(test_list)
    assert result == expected
