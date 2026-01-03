# Contributing Guide

Thank you for your interest in contributing to this project! This guide will help you get started with contributing to our research software.

## Getting Started

### Development Environment Setup

1. **Fork and Clone**: Fork the repository on GitHub and clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/[REPO-NAME].git
   cd [REPO-NAME]
   ```

2. **Create Development Environment**:
   ```bash
   # Option A: Using conda/mamba (recommended)
   conda env create -f environment.yml
   conda activate [project-name]
   pip install -e .

   # Option B: Using pip
   pip install -r requirements-dev.txt
   pip install -e .
   ```

3. **Install Pre-commit Hooks**:
   ```bash
   pre-commit install
   ```

## Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. Code Quality Standards

We maintain high code quality standards with automated tools:

- **Code Formatting**: We use [Black](https://black.readthedocs.io/) with 88-character line length
- **Linting**: [Ruff](https://docs.astral.sh/ruff/) for comprehensive code analysis
- **Type Hints**: Required for all new functions and methods
- **Documentation**: NumPy-style docstrings for all public functions

### 3. Running Tests

```bash
# Run all tests
pytest

# Run specific test types using markers
pytest -m "not slow"          # Skip slow tests
pytest -m "unit"              # Run only unit tests
pytest -m "integration"       # Run only integration tests

# Run tests with coverage
pytest --cov=template_project --cov-report term-missing
```

### 4. Code Quality Checks

Before committing, run the full quality check suite:

```bash
# Format code
black .

# Check and fix linting issues
ruff check --fix .

# Run all pre-commit hooks
pre-commit run --all-files
```

### 5. Scientific Validation

For contributions involving scientific calculations:

- **Reference Methods**: Cite published methods or established practices
- **Validation**: Include test cases with known reference values
- **Units**: Ensure proper handling of units and coordinate systems
- **Documentation**: Document assumptions and limitations

## Types of Contributions

### Bug Fixes
- Use the 🐛 Bug Report template
- Include minimal reproducible example
- Reference any related issues

### New Features
- Use the 💡 Feature Request template first for discussion
- Include scientific motivation and use cases
- Ensure backward compatibility where possible

### Scientific Accuracy Issues
- Use the 🔬 Scientific Accuracy template
- Provide references to correct methods
- Include validation data or test cases

### Documentation
- Follow existing structure and style
- Include examples where appropriate
- Update API documentation for code changes

## Pull Request Process

### 1. Title Convention
Use one of these prefixes:
- `[FEAT]` - New features
- `[FIX]` - Bug fixes
- `[DOC]` - Documentation updates
- `[REFACTOR]` - Code improvements
- `[TEST]` - Tests
- `[CI]` - CI/CD updates
- `[CLEANUP]` - General maintenance

### 2. Description Template
Fill out the pull request template completely, including:
- Summary and motivation
- Type of change checklist
- Testing verification
- Documentation updates
- Scientific validation (if applicable)

### 3. Review Process
- All PRs require at least one review
- Automated checks must pass (tests, linting, type checking)
- Scientific contributions may require domain expert review

## Research Software Engineering Best Practices

### Version Control
- **Conventional Commits**: Use clear, descriptive commit messages
- **Atomic Commits**: One logical change per commit
- **Branch Protection**: Main branch requires PR approval

### Documentation
- **Code Documentation**: NumPy-style docstrings
- **User Documentation**: Clear examples and tutorials
- **Scientific Documentation**: Reference methods and assumptions

### Testing
- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test component interactions
- **Scientific Tests**: Validate against known results
- **Coverage Target**: Aim for >80% test coverage

### Reproducibility
- **Environment Files**: Keep environment.yml and requirements.txt updated
- **Seed Values**: Use fixed random seeds in tests
- **Version Pinning**: Pin critical dependencies

## Scientific Citation Guidelines

When contributing scientific functionality:

1. **Literature Review**: Research existing methods and implementations
2. **Method Documentation**: Clearly document the scientific approach
3. **Reference Implementation**: Compare against established tools where possible
4. **Uncertainty Quantification**: Document limitations and error bounds
5. **Reproducible Examples**: Provide complete working examples

## Getting Help

- **Documentation**: Check our comprehensive docs
- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Report bugs or request features via GitHub Issues
- **Code Review**: Ask questions during the review process

## Recognition

All contributors are recognized in our project documentation. Significant contributions will be acknowledged in publications that use this software.

Thank you for contributing to open research software! 🚀