# anyfloat

Python package for working with arbitrary* precision floating point numbers and their bit-level representations following IEEE-754 rules.

*: currently limited by machine precision, usually 64 bit

## Usage

```bash
pip install anyfloat
```

```python
>>> from anyfloat import FP8_E4M3
>>> FP8_E4M3.float_from_bitstring('01001000')
3.0
```

```python
>>> from anyfloat import FloatingPointSpec
>>> FP13 = FloatingPointSpec(num_mantissa_bits=7, num_exponent_bits=5)
>>> FP13.float_from_bitstring('0100000010000')
3.0
```

For more examples, see `examples/`.

## Development

### Quick start

> Using a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) is recommended

Install requirements:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Install this package in editable mode:

```bash
pip install -e .
```

Install [pre-commit](https://pre-commit.com) hooks:

```bash
pre-commit install
```

## Contributing

This repository follows [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html).
