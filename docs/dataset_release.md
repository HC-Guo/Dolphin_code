# DolphinAI/ReasoningData Dataset Release Guide

## Overview

The **DolphinAI/ReasoningData** dataset is a comprehensive collection of medical ultrasound reasoning data designed for training large language models in medical ultrasound analysis. This dataset supports the two-stage training pipeline of the Dolphin Ultrasound model.

## 🤗 HuggingFace Dataset Information

- **License**: Apache 2.0
- **Language**: English, Chinese (Simplified)
- **Modality**: Vision-Text (Ultrasound Images + Text)

## 📊 Dataset Statistics

| Split | Number of Samples | Description |
|-------|------------------|-------------|
| Train | ~150,000 | Training samples for SFT |
| Test  | ~15,000  | Evaluation samples |
| UARPO  | ~50,000  | Reasoning samples for RL training |

## 🔍 Data Structure

### Sample Format

Each sample in the dataset contains:

```json
{
    "id": "unique_sample_id",
    "images": ["image_path_1.jpg", "image_path_2.jpg"],
    "question": "What pathological findings can you identify in this ultrasound image?",
    "response": "Step-by-step reasoning response...",
    "reasoning_steps": [
        "Step 1: Image quality assessment...",
        "Step 2: Anatomical structure identification...",
        "Step 3: Pathological finding analysis...",
        "Step 4: Conclusion and recommendation..."
    ],
    "metadata": {
        "ultrasound_type": "abdominal",
        "language": "en",
        "difficulty": "medium",
        "diagnostic_category": "pathology_detection"
    }
}
```

### Data Categories

1. **Diagnostic Tasks**
   - Pathology detection
   - Anatomical structure identification
   - Measurement and quantification
   - Image quality assessment

2. **Reasoning Tasks**
   - Step-by-step diagnostic reasoning
   - Differential diagnosis
   - Clinical decision making
   - Report generation

3. **Multimodal Tasks**
   - Image-text alignment
   - Visual question answering
   - Cross-modal reasoning

## 🛠️ Usage Instructions

### Loading the Dataset

```python
from datasets import load_dataset

# Load the complete dataset
dataset = load_dataset("DolphinAI/ReasoningData")

# Load specific split
train_dataset = load_dataset("DolphinAI/ReasoningData", split="train")
test_dataset = load_dataset("DolphinAI/ReasoningData", split="test")
uarpo_dataset = load_dataset("DolphinAI/ReasoningData", split="uarpo")
```

### Data Processing Example

```python
from PIL import Image
import torch
from transformers import AutoProcessor

def process_sample(sample):
    # Load images
    images = [Image.open(img_path) for img_path in sample["images"]]

    # Process with your model's processor
    # processor = AutoProcessor.from_pretrained("your_model")
    # inputs = processor(images=images, text=sample["question"], return_tensors="pt")

    return {
        "images": images,
        "question": sample["question"],
        "response": sample["response"],
        "reasoning_steps": sample["reasoning_steps"]
    }

# Apply processing
processed_dataset = train_dataset.map(process_sample)
```

### Integration with Training Pipeline

#### For SFT Training (LLaMA-Factory)

```yaml
# In your dataset_info.json
"reasoning_data": {
  "hf_hub_url": "DolphinAI/ReasoningData",
  "split": "train",
  "columns": {
    "prompt": "question",
    "query": "question",
    "response": "response",
    "images": "images"
  }
}
```

#### For UARPO Training (EasyR1)

```python
# In your training script
data:
  train_files: "data/huggingface/DolphinAI/ReasoningData@uarpo"
  val_files: "data/huggingface/DolphinAI/ReasoningData@test"
  prompt_key: "question"
  answer_key: "response"
  image_key: "images"
```

## 📁 Dataset Components

### 1. Medical Ultrasound Images
- **Format**: JPG, PNG
- **Resolution**: Variable (typically 512x512 to 1024x1024)
- **Types**: Abdominal, cardiac, obstetric, musculoskeletal, vascular
- **Quality**: Clinical-grade ultrasound images

### 2. Question-Answer Pairs
- **Questions**: Natural language queries about ultrasound findings
- **Answers**: Detailed responses with medical reasoning
- **Languages**: English and Chinese (Simplified)
- **Complexity**: Ranging from basic identification to complex diagnostic reasoning

### 3. Reasoning Chains
- **Structure**: Step-by-step diagnostic reasoning
- **Format**: Ordered list of reasoning steps
- **Content**: Medical logic, visual analysis, clinical correlation

### 4. Metadata
- **Ultrasound Type**: Anatomical region or examination type
- **Difficulty Level**: Easy, medium, hard
- **Language**: en, zh-cn
- **Task Type**: Detection, classification, measurement, reasoning

## 🎯 Applications

### Primary Use Cases
1. **Medical AI Training**: Fine-tuning large language models for ultrasound analysis
2. **Multimodal Research**: Vision-language model development
3. **Clinical Decision Support**: Developing AI-assisted diagnostic tools
4. **Educational Tools**: Training materials for medical students and professionals

### Research Areas
- Medical visual question answering
- Multimodal reasoning in healthcare
- Clinical decision support systems
- Medical image interpretation
- Cross-lingual medical AI

## 🔄 Dataset Updates

### Version History
- **v1.0**: Initial release with 200k+ samples
- **v1.1**: Added reasoning chains and metadata
- **v1.2**: Expanded multilingual support

### Future Updates
- Additional ultrasound modalities
- Enhanced reasoning annotations
- More diverse pathological cases
- Extended multilingual support

## 📋 Data Collection and Annotation

### Data Sources
- De-identified clinical ultrasound images
- Synthetic ultrasound data
- Educational ultrasound datasets
- Research collaborations with medical institutions

### Annotation Process
1. **Medical Expert Review**: Board-certified radiologists and physicians
2. **Quality Assurance**: Multi-stage validation process
3. **Reasoning Annotation**: Structured diagnostic reasoning chains
4. **Multilingual Translation**: Professional medical translation services

### Privacy and Ethics
- All data is de-identified and anonymized
- Compliant with healthcare data regulations
- IRB approval for research use
- Patient privacy protection measures

## ⚖️ License and Usage Terms

### License
- **Type**: Apache 2.0
- **Commercial Use**: Allowed
- **Attribution**: Required

### Usage Restrictions
- Medical use requires appropriate clinical validation
- Not for direct patient care without regulatory approval
- Educational and research use encouraged
- Proper attribution to DolphinAI and contributing institutions

### Citation
```bibtex
@dataset{dolphinai_reasoning_data_2024,
  title={DolphinAI ReasoningData: A Comprehensive Dataset for Medical Ultrasound Analysis and Reasoning},
  author={DolphinAI Research Team},
  year={2024},
  publisher={HuggingFace},
}
```

## 🤝 Contributing

We welcome contributions to expand and improve the dataset:

### How to Contribute
1. **Data Submission**: Submit new ultrasound cases with annotations
2. **Quality Improvement**: Report data quality issues or suggest improvements
3. **Multilingual Expansion**: Provide translations or native language annotations
4. **Validation**: Help validate existing annotations

### Contribution Guidelines
- Follow medical data privacy guidelines
- Ensure data quality and accuracy
- Provide proper documentation
- Include appropriate metadata

## 📞 Support and Contact

### Technical Support
- **Email**: dataset-support@dolphinai.com

### Research Collaboration
- **Academic Partnerships**: research@dolphinai.com
- **Clinical Collaboration**: clinical@dolphinai.com
- **Industry Partnerships**: partnerships@dolphinai.com

---

## 🏥 Medical Disclaimer

This dataset is intended for research and educational purposes only. It should not be used for direct clinical diagnosis or patient care without appropriate validation and regulatory approval. Always consult with qualified healthcare professionals for medical decisions.