import pytest


@pytest.mark.xfail(reason="expecting fail and I get it")
def test_math_fail_as_expected():
    num1, num2 = 5, 10
    assert num1 * num2 != num2 * num1
    print("Test ends now")


@pytest.mark.xfail(reason="expecting NonStrict fail")
def test_math_pass_but_expects_fail():
    assert 1 + 1 == 2


@pytest.mark.xfail(reason="expecting Strict fail", strict=True)
def test_string_pass_but_expect_strict_fail():
    str1 = "abc"
    str2 = str1.capitalize()

    assert "abc" != str2