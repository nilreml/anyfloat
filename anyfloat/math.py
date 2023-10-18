from math import copysign, frexp


def floats_from_bits(*,
                     sign_bit: str,
                     mantissa_bits: str,
                     exponent_bits: str,
                     num_mantissa_bits: int,
                     num_exponent_bits: int,
                     exponent_bias: int,
                     ) -> tuple[float, int, float, int]:
    """
    Assemble an arbitrary precision floating point number from it's components following IEEE-754 rules.

    Args:
        sign_bit           : '1' for positive, '0' for negative
        mantissa_bits      : Bit representation of mantissa (length = num_mantissa_bits)
        exponent_bits      : Bit representation of exponent (length = num_exponent_bits)
        num_mantissa_bits  : Number of stored bits in mantissa (excluding the implicit bit)
        num_exponent_bits  : Number of stored bits in exponent
        exponent_bias      : Bias of exponent (negative)

    Returns:
        result             : Assembled floating point number
        sign               : '1' for positive, '-1' for negative
        mantissa           : Encoded mantissa of floating point number
        exponent           : Encoded exponent of floating point number
    """

    if sign_bit not in ['0', '1']:
        msg = f"sign_bit='{sign_bit}' is not a str with value '0' or '1'"
        raise ValueError(msg)

    if len(mantissa_bits) != num_mantissa_bits:
        msg = f"mantissa_bits='{mantissa_bits}' is not a string of length num_mantissa_bits={num_mantissa_bits}"
        raise ValueError(msg)

    if len(exponent_bits) != num_exponent_bits:
        msg = f"exponent_bits='{exponent_bits}' is not a string of length num_exponent_bits={num_exponent_bits}"
        raise ValueError(msg)

    sign = 1 if sign_bit == '0' else -1

    exponent = int(exponent_bits, 2) + exponent_bias
    exponent_max = 2 ** num_exponent_bits - 1  # max encodable, ignoring bias
    mantissa_max = 2 ** num_mantissa_bits - 1  # max encodable, ignoring bias

    # Add implicit leading bit to mantissa if not denormalized (exponent_bits > 0)
    mantissa_bias = 0.0
    if exponent > exponent_bias:
        mantissa_bias = 1.0

    mantissa = mantissa_bias + float(int(mantissa_bits, 2)) / float(mantissa_max + 1)

    result: float = float(sign) * mantissa * 2.**float(exponent)

    # Handle NaN and infinity
    if int(exponent_bits, 2) >= exponent_max:
        if int(mantissa_bits, 2) == 0:
            result = float(sign) * float('inf')
        else:
            result = float('nan')

    # Handle zero:
    if mantissa == 0.0:
        exponent = 0

    return result, sign, mantissa, exponent


def bits_from_float(*,
                    x: float,
                    num_mantissa_bits: int,
                    num_exponent_bits: int,
                    exponent_bias: int,
                    allow_underflow: bool = True,
                    allow_overflow: bool = True,
                    ) -> tuple[str, str, str]:
    """
    Disassemble an arbitrary precision floating point number into it's components following IEEE-754 rules.

    Args:
        x                   : Floating point number to disassemble
        num_mantissa_bits   : Number of stored bits in mantissa (excluding the implicit bit)
        num_exponent_bits   : Number of stored bits in exponent
        exponent_bias       : Bias of exponent (negative)
        allow_underflow     : Allow underflow
        allow_overflow      : Allow overflow

    Returns:
        sign_bit            : '1' for positive, '0' for negative
        mantissa_bits       : Bit representation of mantissa (length = num_mantissa_bits)
        exponent_bits       : Bit representation of exponent (length = num_exponent_bits)
    """

    # exponent_max = 2 ** num_exponent_bits - 1  # max encodable, ignoring bias
    mantissa_max = 2 ** num_mantissa_bits - 1  # max encodable, ignoring bias

    # TODO: handle underflow
    # TODO: handle overflow
    # # Handle exponent underflow
    # if exponent < 0:
    #     exponent = 0
    #     if not allow_underflow:
    #         raise ValueError(f"Exponent underflow: exponent={exponent} < 0")

    # # Handle exponent overflow
    # if exponent > exponent_max:
    #     exponent = exponent_max  # infinity
    #     if not allow_overflow:
    #         raise ValueError(f"Exponent overflow: exponent={exponent} > exponent_max={exponent_max}")

    # Extract mantissa and exponent
    mantissa, exponent = frexp(x)

    # print(f"frexp() mantissa : {mantissa:.16e}")
    # print(f"frexp() exponent : {exponent}")

    mantissa_bias = 0.0

    if exponent > exponent_bias:
        exponent -= 1
        mantissa *= 2.0
        mantissa_bias = 1.0

    print(f'mantissa : {mantissa:.16e}')
    print(f'exponent : {exponent}')

    # TODO: flip sign of exponent bias

    exponent_encoded = exponent - exponent_bias
    mantissa_encoded = int((mantissa - mantissa_bias) * (mantissa_max + 1))

    # Extract exponent bits
    exponent_bits = f'{exponent_encoded:0{num_exponent_bits}b}'

    # Extract mantissa bits
    mantissa_bits = f'{mantissa_encoded:0{num_mantissa_bits}b}'

    # Extract sign bit, signed zero support is platform dependent
    sign_bit = '0'
    if copysign(1.0, x) < 0:
        sign_bit = '1'

    return sign_bit, mantissa_bits, exponent_bits
