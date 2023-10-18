from typing import Optional

from .math import bits_from_float, floats_from_bits


class FloatingPointSpec:
    """
    Specification of arbitrary precision floating point numbers

    Typical usage example:
        ```
        >>> FP13 = FloatingPointSpec(num_mantissa_bits=6, num_exponent_bits=5)
        >>> FP13.float_from_bitstring('010000010000')
        2.5
        ```
    """

    num_mantissa_bits: int
    num_exponent_bits: int
    exponent_bias: int

    def __init__(self,
                 *,
                 num_mantissa_bits: int,
                 num_exponent_bits: int,
                 exponent_bias: Optional[int] = None,
                 ) -> None:
        """
        Specification for arbitrary precision floating point numbers.

        Args:
            num_mantissa_bits           : Number of stored bits in mantissa(excluding the implicit leading bit)
            num_exponent_bits           : Number of stored bits in exponent
            exponent_bias               : Bias of exponent (negative, default follows IEEE-754 rules)
        """

        if exponent_bias:
            self.exponent_bias = exponent_bias
        else:
            self.exponent_bias = 1 - 2**(num_exponent_bits - 1)

        self.num_mantissa_bits = num_mantissa_bits
        self.num_exponent_bits = num_exponent_bits

    def floats_from_bitstrings(self, s: str, m: str, e: str) -> tuple[float, int, float, int]:
        """
        Assemble an arbitrary precision floating point number from it's components following IEEE-754 rules where possible.

        Args:
            s : '1' for positive, '0' for negative
            m : Bit representation of mantissa (length = num_mantissa_bits)
            e : Bit representation of exponent (length = num_exponent_bits)

        Returns:
            result             : Assembled floating point number
            sign               : '1' for positive, '-1' for negative
            mantissa           : Encoded mantissa of floating point number
            exponent           : Encoded exponent of floating point number
        """

        return floats_from_bits(
            sign_bit=s,
            mantissa_bits=m,
            exponent_bits=e,
            num_mantissa_bits=self.num_mantissa_bits,
            num_exponent_bits=self.num_exponent_bits,
            exponent_bias=self.exponent_bias,
        )

    def floats_from_bitstring(self, bitstring: str) -> tuple[float, int, float, int]:
        """
        Assemble an arbitrary precision floating point number from it's components following IEEE-754 rules where possible.

        Args:
            bitstring : sign_bit + mantissa_bits + exponent_bits

        Returns:
            result             : Assembled floating point number
            sign               : '1' for positive, '-1' for negative
            mantissa           : Encoded mantissa of floating point number
            exponent           : Encoded exponent of floating point number
        """
        return floats_from_bits(
            sign_bit=bitstring[0],
            mantissa_bits=bitstring[1:1 + self.num_mantissa_bits],
            exponent_bits=bitstring[1 + self.num_mantissa_bits:],
            num_mantissa_bits=self.num_mantissa_bits,
            num_exponent_bits=self.num_exponent_bits,
            exponent_bias=self.exponent_bias,
        )

    def float_from_bitstrings(self, *, s: str, m: str, e: str) -> float:
        return self.floats_from_bitstrings(s=s, m=m, e=e)[0]

    def float_from_bitstring(self, bitstring: str) -> float:
        return self.floats_from_bitstring(bitstring)[0]

    def bitstrings_from_float(self, x: float) -> tuple[str, str, str]:
        """
        Disassemble an arbitrary precision floating point number into it's components following IEEE-754 rules where possible.

        Args:
            x : Floating point number to disassemble

        Returns:
            sign_bit      : '1' for positive, '0' for negative
            mantissa_bits : Bit representation of mantissa (length = num_mantissa_bits)
            exponent_bits : Bit representation of exponent (length = num_exponent_bits)
        """

        return bits_from_float(
            x=x,
            num_mantissa_bits=self.num_mantissa_bits,
            num_exponent_bits=self.num_exponent_bits,
            exponent_bias=self.exponent_bias,
        )

    def bitstring_from_float(self, x: float) -> str:
        """
        Disassemble an arbitrary precision floating point number into it's components following IEEE-754 rules where possible.

        Args:
            x : Floating point number to disassemble

        Returns:
            sign_bit + mantissa_bits + exponent_bits
        """

        s, m, e = self.bitstrings_from_float(x)
        return s + m + e
