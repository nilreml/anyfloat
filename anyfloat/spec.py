from typing import Optional

from .math import bits_from_float, float_from_bits


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

    def float_from_bitstrings(self, s: str, m: str, e: str) -> float:
        """
        Assemble an arbitrary precision floating point number from it's components following IEEE-754 rules where possible.

        Args:
            s : '1' for positive, '0' for negative
            m : Bit representation of mantissa (length = num_mantissa_bits)
            e : Bit representation of exponent (length = num_exponent_bits)

        Returns:
            Assembled floating point number
        """

        return float_from_bits(
            sign_bit=s,
            mantissa_bits=m,
            exponent_bits=e,
            num_mantissa_bits=self.num_mantissa_bits,
            num_exponent_bits=self.num_exponent_bits,
            exponent_bias=self.exponent_bias,
        )

    def float_from_bitstring(self, bitstring: str) -> float:
        return float_from_bits(
            sign_bit=bitstring[0],
            mantissa_bits=bitstring[1:1 + self.num_mantissa_bits],
            exponent_bits=bitstring[1 + self.num_mantissa_bits:],
            num_mantissa_bits=self.num_mantissa_bits,
            num_exponent_bits=self.num_exponent_bits,
            exponent_bias=self.exponent_bias,
        )

    def bitstrings_from_float(self, x: float) -> tuple[str, str, str]:
        """
        Disassemble an arbitrary precision floating point number into it's components following IEEE-754 rules where possible.

        Args:
            x : Floating point number to disassemble

        Returns:
            sign_bit, mantissa_bits, exponent_bits
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
            number: Floating point number to disassemble

        Returns:
            bitstring
        """

        return self.bitstrings_from_float(x)[0]
