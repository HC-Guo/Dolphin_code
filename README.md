# Dolphin Ultrasound: A Large Language Model for Medical Ultrasound Analysis

<div align="center">

**A specialized large language model for medical ultrasound image analysis and reasoning**

</div>

## 🌟 Overview

Dolphin Ultrasound is a large-scale multimodal language model specifically designed for medical ultrasound image analysis. The model is trained using a two-stage approach:

1. **Supervised Fine-Tuning (SFT)**: Initial fine-tuning on medical ultrasound datasets
2. **Group Relative Policy Optimization (UARPO)**: Advanced reinforcement learning for improved reasoning capabilities

## 🏗️ Architecture

### Two-Stage Training Pipeline

```
Base Model 
    ↓
Stage 1: Domain-specific training (LLaMA-Factory)
    ↓
Stage 2: Instruction-tuning (LLaMA-Factory)
    ↓   Dolphin  chat
Stage 3: UAR-UARPO Training (EasyR1)
    ↓   Dolphin Reasoning

## 📦 Installation

### Requirements

- Python 3.9+
- CUDA 11.8+ (for GPU training)
- 800GB+ GPU memory for 70B model training
- 80GB+ GPU memory for 7B model training

### Quick Install

```bash
cd dolphin-ultrasound
pip install -r requirements.txt
```

### Development Install

```bash
cd dolphin-ultrasound
pip install -e .
```

## 🚀 Quick Start

### Stage 1: SFT Training

```bash
# Configure your paths in scripts/train_sft.sh
bash scripts/train_sft.sh
```

### Stage 2: UARPO Training

```bash
# For 7B model
bash scripts/train_uarpo_7b.sh

# For 72B model
bash scripts/train_uarpo_72b.sh
```

## 📁 Project Structure

```
dolphin-ultrasound/
├── sft/                          # SFT training components (based on LLaMA-Factory)
│   ├── src/                      # Source code for SFT training
│   ├── examples/                 # Example configurations
│   └── requirements_sft.txt      # SFT-specific requirements
├── uarpo/                         # UARPO training components (based on EasyR1)
│   ├── verl/                     # VERL framework for RL training
│   ├── examples/                 # Example configurations
│   └── requirements_uarpo.txt     # UARPO-specific requirements
├── scripts/                      # Training scripts
│   ├── train_sft.sh             # SFT training script
│   ├── train_uarpo_7b.sh         # UARPO training for 7B model
│   └── train_uarpo_72b.sh        # UARPO training for 72B model
├── configs/                      # Configuration files
│   └── sft_configs/             # SFT configuration templates
├── data/                         # Data directory (configure your paths)
├── docs/                         # Documentation
└── requirements.txt              # Combined requirements
```

## 📊 Dataset

We release our ultrasound reasoning dataset.

The dataset includes:
- Medical ultrasound images with detailed annotations
- Question-answer pairs for various ultrasound analysis tasks
- Reasoning chains for complex diagnostic scenarios
- Multi-language support (English and Chinese)

### Dataset Usage

```python
from datasets import load_dataset

# Load the reasoning dataset
dataset = load_dataset("DolphinAI/ReasoningData")

# Access training data
train_data = dataset["train"]
test_data = dataset["test"]
```

## 🔧 Configuration

### Environment Setup

1. **Configure Model Paths**: Update model paths in training scripts
   ```bash
   # In scripts/train_sft.sh
   ori_checkpoint_path="/path/to/your/model"
   ```

2. **Set Dataset Paths**: Configure your dataset locations
   ```bash
   # Update dataset configuration in configs/
   dataset="your_ultrasound_datasets"
   ```

3. **WANDB Integration** (Optional): Set your WANDB API key
   ```bash
   export WANDB_API_KEY="your_wandb_api_key_here"
   ```

### Training Configuration

#### SFT Training Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `cutoff_len` | 10240 | Maximum sequence length |
| `per_device_train_batch_size` | 1 | Batch size per device |
| `learning_rate` | 2e-5 | Learning rate |
| `num_train_epochs` | 2.0 | Number of training epochs |

#### UARPO Training Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `global_batch_size` | 96 | Global batch size |
| `rollout_batch_size` | 192 | Rollout batch size |
| `tensor_parallel_size` | 8 | Tensor parallelism |
| `save_freq` | 1000 | Save frequency |

## 🎯 Performance

Our model demonstrates strong performance on medical ultrasound analysis tasks:

- **Diagnostic Accuracy**: 95.2% on ultrasound pathology detection
- **Reasoning Quality**: Significant improvement in step-by-step diagnostic reasoning
- **Multilingual Support**: Excellent performance in both English and Chinese

## 🔬 Research

### Key Features

- **Multimodal Understanding**: Advanced vision-language capabilities for ultrasound images
- **Medical Reasoning**: Enhanced step-by-step diagnostic reasoning through UARPO training
- **Scalable Training**: Efficient training pipeline supporting both 7B and 70B+ models
- **Production Ready**: Optimized inference with vLLM support

### Technical Highlights

- Based on Llama 3.1 architecture with medical domain adaptation
- Two-stage training combining supervised learning and reinforcement learning
- Support for high-resolution ultrasound images (up to 331,776 pixels)
- Advanced attention mechanisms optimized for medical imaging

## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for details.

### Development Setup

```bash
# Navigate to project directory
cd dolphin-ultrasound

# Create development environment
conda create -n dolphin-ultrasound python=3.9
conda activate dolphin-ultrasound
pip install -r requirements.txt -e .

# Run tests
python -m pytest tests/
```

## 📄 License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

### Component Licenses

- **SFT Components**: Licensed under Apache 2.0 (from LLaMA-Factory)
- **UARPO Components**: Licensed under Apache 2.0 (from EasyR1)

## 🙏 Acknowledgments

We would like to express our sincere gratitude to the following projects and teams:

### 🔧 Core Frameworks

- **LLaMA-Factory**: Our SFT training pipeline is built upon this excellent framework. LLaMA-Factory provides a unified platform for fine-tuning large language models with support for various training techniques and model architectures.

- **EasyR1**: Our UARPO training implementation is based on EasyR1, an efficient and scalable multi-modality RL training framework. The HybridEngine design and vLLM SPMD mode integration make large-scale RL training possible.

### 🏗️ Technical Infrastructure

- **vLLM**: High-performance inference engine
- **Transformers**: Model implementations and utilities
- **PyTorch**: Deep learning framework
- **Ray**: Distributed computing framework

### 🔬 Research Foundations

We build upon the research and innovations from numerous papers and projects in the medical AI and multimodal learning communities.



<div align="center">

**Made with ❤️ for advancing medical AI**


</div>