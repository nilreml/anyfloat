import math

from anyfloat import FP32


def test_float_from_bitstrings_positive_infinity():
    sign_bit = '0'
    mantissa_bits = '00000000000000000000000'
    exponent_bits = '11111111'

    result = FP32.float_from_bitstrings(
        s=sign_bit,
        m=mantissa_bits,
        e=exponent_bits,
    )

    assert result == float('inf')


def test_float_from_bitstrings_negative_infinity():
    sign_bit = '1'
    mantissa_bits = '00000000000000000000000'
    exponent_bits = '11111111'

    result = FP32.float_from_bitstrings(
        s=sign_bit,
        m=mantissa_bits,
        e=exponent_bits,
    )

    assert result == float('-inf')


def test_float_from_bitstrings_positive_nan():
    sign_bit = '0'
    mantissa_bits = '00000000000000000000001'
    exponent_bits = '11111111'

    result = FP32.float_from_bitstrings(
        s=sign_bit,
        m=mantissa_bits,
        e=exponent_bits,
    )

    assert math.isnan(result)


def test_float_from_bitstrings_negative_nan():
    sign_bit = '1'
    mantissa_bits = '00000000000000000000001'
    exponent_bits = '11111111'

    result = FP32.float_from_bitstrings(
        s=sign_bit,
        m=mantissa_bits,
        e=exponent_bits,
    )

    assert math.isnan(result)

# TODO: implement and test denormalized floats

# TODO: add parametric tests
