# Aptamer Generator

A Python package for generating DNA aptamer candidates with controlled GC content using AI-driven methods.

## Features

- **Configurable Generation**: Control sequence length and GC content ranges
- **Reproducibility**: Seed-based random number generation for consistent results
- **Validation**: Built-in GC content validation using Biopython
- **Testing**: Full test coverage with pytest
- **Packaging**: Easy installation via pip/PyPI

## Installation

### From GitHub

```
pip install git+https://github.com/yourusername/aptamer-generator.git
```

### Local Development

```
git clone https://github.com/yourusername/aptamer-generator.git
cd aptamer-generator
pip install -e .[test] # Editable mode with test dependencies
```


## Usage

### Basic Example

```

from aptamer_generator import AptamerGenerator

# Initialize generator with seed

generator = AptamerGenerator(seed=42)

# Generate 5 sequences of length 40 with 45-55% GC

sequences = generator.generate_candidates(
num=5,
length=40,
gc_range=(0.45, 0.55)
)

# Print results

for i, seq in enumerate(sequences, 1):
print(f"Sequence {i}: {seq}")

```

### Advanced Usage
```


# Generate sequences with strict GC constraints

high_gc_seqs = generator.generate_candidates(
num=10,
gc_range=(0.6, 0.7)
)

```

## Development

### Running Tests
```

pytest -v --cov=aptamer_generator --cov-report=term-missing

```

### Building the Package
```

python -m build

```

### Uploading to PyPI (Optional)
```

twine upload dist/*

```

## API Reference

### `AptamerGenerator`
```

class AptamerGenerator(seed=None)

```
- `seed`: Integer seed for reproducible results

#### Methods
```

.generate_candidates(num=10, length=40, gc_range=(0.4, 0.6))

```
- `num`: Number of sequences to generate
- `length`: Nucleotide length per sequence
- `gc_range`: Tuple of (min_gc, max_gc) as fractions (0.0-1.0)

## Technical Details

### Dependencies
- Python >=3.8
- numpy >=1.21
- biopython >=1.79

### Algorithm
Uses rejection sampling with the following steps:
1. Random DNA sequence generation
2. GC content calculation
3. Constraint validation
4. Repeat until requested number of valid sequences are generated

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details




