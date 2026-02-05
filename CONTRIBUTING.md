# Contributing to Dolphin Ultrasound

We welcome contributions to the Dolphin Ultrasound project! This document provides guidelines for contributing to our medical AI project.

## 🤝 How to Contribute

### Types of Contributions

1. **Code Contributions**
   - Bug fixes
   - Feature implementations
   - Performance improvements
   - Documentation improvements

2. **Data Contributions**
   - New ultrasound datasets
   - Annotation improvements
   - Data quality enhancements

3. **Research Contributions**
   - Model improvements
   - Training techniques
   - Evaluation methods

4. **Documentation**
   - API documentation
   - Tutorials and examples
   - Best practices guides

## 🚀 Getting Started

### Development Setup

1. **Fork the Repository**
   ```bash
   # Fork the repo on GitHub, then clone your fork
   cd dolphin-ultrasound
   ```

2. **Set Up Development Environment**
   ```bash
   # Create a conda environment
   conda create -n dolphin-dev python=3.9
   conda activate dolphin-dev

   # Install dependencies
   pip install -r requirements.txt
   pip install -e .

   # Install development dependencies
   pip install pytest black flake8 pre-commit
   ```

3. **Set Up Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

### Making Changes

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-description
   ```

2. **Make Your Changes**
   - Follow the coding standards (see below)
   - Add tests for new functionality
   - Update documentation as needed

3. **Test Your Changes**
   ```bash
   # Run tests
   python -m pytest tests/

   # Run linting
   black --check .
   flake8 .
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   # Then create a PR on GitHub
   ```

## 📝 Coding Standards

### Python Code Style

- **Formatter**: Black (line length: 88)
- **Linter**: Flake8
- **Import Sorting**: isort
- **Type Hints**: Use type hints for function signatures

### Code Organization

```python
# Example function structure
from typing import List, Optional, Dict, Any

import torch
from transformers import AutoModel

def process_ultrasound_images(
    images: List[str],
    model: AutoModel,
    device: Optional[str] = None
) -> Dict[str, Any]:
    """Process ultrasound images with the given model.

    Args:
        images: List of image file paths
        model: The model to use for processing
        device: Device to run inference on

    Returns:
        Dictionary containing processing results

    Raises:
        ValueError: If images list is empty
    """
    if not images:
        raise ValueError("Images list cannot be empty")

    # Implementation here
    return {"results": "processed"}
```

### Documentation Standards

- **Docstrings**: Google-style docstrings
- **Comments**: Clear, concise comments for complex logic
- **README**: Update README for new features
- **Type Hints**: Include type hints for better code clarity

## 🔬 Medical AI Guidelines

### Data Handling

1. **Privacy First**
   - Never commit real patient data
   - Use synthetic or properly anonymized data
   - Follow HIPAA and GDPR guidelines

2. **Data Quality**
   - Ensure high-quality annotations
   - Validate medical accuracy
   - Include diverse patient populations

### Model Development

1. **Validation Requirements**
   - Cross-validation on diverse datasets
   - Clinical validation when applicable
   - Bias and fairness assessments

2. **Safety Considerations**
   - Include uncertainty quantification
   - Implement safety checks
   - Clear limitation documentation

## 🧪 Testing Guidelines

### Test Structure

```bash
tests/
├── unit/           # Unit tests
├── integration/    # Integration tests
├── data/          # Test data (synthetic only)
└── fixtures/      # Test fixtures
```

### Test Categories

1. **Unit Tests**
   - Individual function testing
   - Mock external dependencies
   - Fast execution (< 1s per test)

2. **Integration Tests**
   - End-to-end workflow testing
   - Real model inference testing
   - Longer execution acceptable

3. **Data Tests**
   - Dataset validation
   - Data pipeline testing
   - Format compliance

### Writing Tests

```python
import pytest
import torch
from unittest.mock import Mock, patch

from dolphin_ultrasound import UltrasoundProcessor

def test_ultrasound_processor_initialization():
    """Test UltrasoundProcessor initialization."""
    processor = UltrasoundProcessor(model_path="test_model")
    assert processor.model_path == "test_model"

@patch('dolphin_ultrasound.load_model')
def test_process_with_mock_model(mock_load_model):
    """Test processing with mocked model."""
    mock_model = Mock()
    mock_load_model.return_value = mock_model

    processor = UltrasoundProcessor("test_model")
    result = processor.process(["test_image.jpg"])

    assert result is not None
    mock_model.predict.assert_called_once()
```

## 📊 Pull Request Process

### PR Checklist

- [ ] Branch is up to date with main
- [ ] All tests pass
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Changes are covered by tests
- [ ] PR description clearly explains changes

### PR Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Added new tests
- [ ] All tests pass
- [ ] Manual testing completed

## Medical AI Considerations
- [ ] No patient data included
- [ ] Clinical validation considered
- [ ] Safety implications addressed

## Checklist
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Breaking changes documented
```

### Review Process

1. **Automated Checks**
   - CI/CD pipeline runs
   - Code quality checks
   - Test coverage analysis

2. **Human Review**
   - Code review by maintainers
   - Medical accuracy review (for clinical features)
   - Documentation review

3. **Approval and Merge**
   - At least one maintainer approval
   - All checks passing
   - Squash and merge preferred

## 🏥 Medical Contributions

### Clinical Expertise

We welcome contributions from medical professionals:

1. **Clinical Validation**
   - Review model outputs for medical accuracy
   - Provide clinical context and insights
   - Validate diagnostic reasoning chains

2. **Dataset Annotation**
   - Medical image annotation
   - Diagnostic reasoning annotation
   - Quality assurance for medical content

3. **Use Case Development**
   - Identify clinical applications
   - Define evaluation metrics
   - Develop clinical workflows

### Collaboration Guidelines

- Respect patient privacy at all times
- Follow medical ethics guidelines
- Collaborate with technical team on implementation
- Provide clear medical documentation

## 🌍 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Maintain professional communication

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: Sensitive or private matters

### Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Academic publications (when applicable)
- Project acknowledgments

## 📈 Development Roadmap

### Current Priorities

1. **Model Performance**
   - Improve diagnostic accuracy
   - Reduce inference latency
   - Enhance multilingual support

2. **Training Pipeline**
   - Optimize SFT training
   - Improve UARPO implementation
   - Add more evaluation metrics

3. **Documentation**
   - Comprehensive API docs
   - Tutorial development
   - Best practices guides

### Future Goals

- Support for more ultrasound modalities
- Real-time inference optimization
- Clinical deployment tools
- Extended multilingual support

## ❓ Getting Help

### Resources

- **Documentation**: Check existing docs first
- **Issues**: Search existing issues
- **Discussions**: Ask questions in GitHub Discussions

### Contacts

- **Technical Questions**: Create GitHub issue
- **Medical Questions**: clinical@dolphinai.com
- **General Inquiries**: contribute@dolphinai.com

## 📄 License

By contributing to Dolphin Ultrasound, you agree that your contributions will be licensed under the Apache License 2.0.

---

Thank you for contributing to Dolphin Ultrasound! Your contributions help advance medical AI and improve patient care. 🏥❤️