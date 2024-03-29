from anyfloat import FP8_E4M3, FloatingPointSpec

print(FP8_E4M3.float_from_bitstring('01001000'))

FP4 = FloatingPointSpec(num_mantissa_bits=1, num_exponent_bits=2)
print(FP4.float_from_bitstring('0110'))
print(FP4.bitstring_from_float(3.0))

print()

FP13 = FloatingPointSpec(num_mantissa_bits=7, num_exponent_bits=5)
print(FP13.float_from_bitstring('0100000010000'))

FP4 = FloatingPointSpec(num_mantissa_bits=1, num_exponent_bits=2)
x, s, m, e = FP4.floats_from_bitstrings(s='0', m='1', e='01')
print(x, s, m, e)
b = FP4.bitstrings_from_float(x)
print(b)


# FP6 = FloatingPointSpec(num_mantissa_bits=3, num_exponent_bits=2)
# x = FP6.float_from_bitstrings(s='0', m='001', e='00')
# print(x)
# b = FP6.bitstrings_from_float(x)
# print(b)


FP32 = FloatingPointSpec(num_mantissa_bits=23, num_exponent_bits=8)
x = FP32.float_from_bitstrings(s='0', m='10000000000000000000001', e='00000001')
print(x)
b = FP32.bitstrings_from_float(x)
print(b)
