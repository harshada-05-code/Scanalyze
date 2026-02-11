# 🏥 Medical Image Analysis System

An AI-powered medical image analysis tool for chest X-ray classification and analysis.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31-red.svg)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.15-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Features

- **Image Upload & Analysis**: Support for PNG, JPG, JPEG formats
- **Disease Classification**: Detects Normal, Pneumonia, COVID-19, Tuberculosis
- **Confidence Scores**: Provides probability distributions for each diagnosis
- **Visual Heatmaps**: Highlights regions of interest in the X-ray
- **Clinical Reports**: Generates downloadable analysis reports
- **Interactive UI**: User-friendly Streamlit interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/medical-image-analysis.git
cd medical-image-analysis
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Demo

```bash
cd demo
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
medical-image-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── demo/
│   ├── app.py                 # Main Streamlit application
│   └── sample_images/         # Sample X-ray images
├── src/
│   ├── __init__.py
│   ├── model.py              # Model architecture
│   ├── preprocessing.py      # Image preprocessing utilities
│   └── utils.py              # Helper functions
├── notebooks/
│   └── exploration.ipynb     # Data exploration notebook
├── data/                     # Training data directory
└── models/                   # Saved models directory
```

## 🔧 Usage

### Basic Usage

1. Launch the application
2. Upload a chest X-ray image or use sample image
3. Wait for analysis to complete
4. Review results and confidence scores
5. Download the clinical report if needed

### API Usage (Coming Soon)

```python
from src.model import MedicalImageAnalyzer

analyzer = MedicalImageAnalyzer()
results = analyzer.predict('path/to/xray.jpg')
print(results)
```

## 🧠 Model Information

### Current Implementation
- **Base Model**: DenseNet121 (pre-trained on ImageNet)
- **Input Size**: 224x224 pixels
- **Output Classes**: 4 (Normal, Pneumonia, COVID-19, Tuberculosis)

### Future Enhancements
- Custom trained model on chest X-ray datasets
- Support for more diseases and conditions
- DICOM file format support
- Batch processing capabilities
- Model explainability (Grad-CAM)

## 📊 Datasets (For Training)

Recommended datasets for training production models:

1. **ChestX-ray14**: NIH dataset with 14 pathologies
2. **COVID-19 Radiography Database**: Kaggle dataset
3. **RSNA Pneumonia Detection**: Kaggle competition dataset
4. **TB Chest X-ray Database**: Tuberculosis dataset

## 🛠️ Development Roadmap

- [x] Basic Streamlit interface
- [x] Image upload and display
- [x] Mock classification results
- [x] Visualization with heatmaps
- [x] Report generation
- [ ] Train custom model on medical datasets
- [ ] Add DICOM support
- [ ] Implement Grad-CAM visualization
- [ ] Add user authentication
- [ ] Deploy to cloud (AWS/GCP/Azure)
- [ ] REST API development
- [ ] Mobile app integration

## ⚠️ Disclaimer

**IMPORTANT**: This application is for research and educational purposes only. It should NOT be used for actual medical diagnosis or treatment decisions. Always consult with qualified healthcare professionals for medical advice.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

Your Name - wankhedeharshada14@gmail.com

Project Link: [https://github.com/yourusername/medical-image-analysis](https://github.com/yourusername/medical-image-analysis)

## 🙏 Acknowledgments

- TensorFlow and Keras teams
- Streamlit for the amazing framework
- Medical imaging research community
- Open-source datasets providers

## 📚 References

1. Rajpurkar, P., et al. (2017). "CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays"
2. Wang, X., et al. (2017). "ChestX-ray8: Hospital-scale Chest X-ray Database"
3. Cohen, J.P., et al. (2020). "COVID-19 Image Data Collection"

---

**Built with ❤️ for better healthcare**
