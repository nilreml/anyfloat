from anyfloat import FloatingPointSpec

# FP4 = FloatingPointSpec(num_mantissa_bits=1, num_exponent_bits=2)
# x = FP4.float_from_bitstrings(s='0', m='1', e='10')
# print(x)
# b = FP4.bitstrings_from_float(x)
# print(b)


# FP6 = FloatingPointSpec(num_mantissa_bits=3, num_exponent_bits=2)
# x = FP6.float_from_bitstrings(s='0', m='001', e='00')
# print(x)
# b = FP6.bitstrings_from_float(x)
# print(b)


FP32 = FloatingPointSpec(num_mantissa_bits=23, num_exponent_bits=8, ensure_power_of_two_storage=True)
x = FP32.float_from_bitstrings(s='0', m='10000000000000000000001', e='00000001')
print(x)
b = FP32.bitstrings_from_float(x)
print(b)
