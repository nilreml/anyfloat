# Arbitrary precision floating point numbers

This Python package allows working with arbitrary* precision floating point numbers and their bit-level representations following IEEE-754 rules.

*: currently limited by machine precision, usually 64 bit

## Usage

```bash
pip install floatingpoint
```

```python
>>> FP13 = FloatingPointSpec(num_mantissa_bits=6, num_exponent_bits=5)
>>> FP13.float_from_bitstring('010000010000')
2.5
```

For more examples, see `examples/`.

## Development

### Quick start using devcontainers (preferred)

Create an empty workspace using an [IDE with devcontainers support](https://containers.dev/supporting) and add this repository's folder.

The devcontainer will automatically be built and managed by your IDE.

### Otherwise

> Using a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) is recommended.

Install requirements:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Install this module in editable mode:

```bash
pip install -e .
```

Install [pre-commit](https://pre-commit.com) hooks (recommended):

```bash
pre-commit install
```

## Contributing

This repository follows [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html).
