from .spec import FloatingPointSpec

FP64 = FloatingPointSpec(num_mantissa_bits=52, num_exponent_bits=11)
FP32 = FloatingPointSpec(num_mantissa_bits=23, num_exponent_bits=8)
FP16 = FloatingPointSpec(num_mantissa_bits=10, num_exponent_bits=5)
BF16 = FloatingPointSpec(num_mantissa_bits=7, num_exponent_bits=8)
FP8_E5M2 = FloatingPointSpec(num_mantissa_bits=2, num_exponent_bits=5)
FP8_E4M3 = FloatingPointSpec(num_mantissa_bits=3, num_exponent_bits=4)
