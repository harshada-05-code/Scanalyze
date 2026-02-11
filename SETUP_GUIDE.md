# Quick Setup Guide - Medical Image Analysis

## For 3 PM Demo Submission

### Step 1: GitHub Setup (5 minutes)

1. **Create GitHub Repository**
   - Go to https://github.com/new
   - Repository name: `medical-image-analysis`
   - Description: "AI-powered medical image analysis for chest X-ray classification"
   - Make it Public
   - Don't initialize with README (we have one)
   - Click "Create repository"

2. **Push Code to GitHub**
   ```bash
   cd medical-image-analysis
   git init
   git add .
   git commit -m "Initial commit: Medical Image Analysis demo"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/medical-image-analysis.git
   git push -u origin main
   ```

### Step 2: Local Testing (5 minutes)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Demo**
   ```bash
   cd demo
   streamlit run app.py
   ```

3. **Test Features**
   - Upload an X-ray image (or use sample)
   - Verify analysis works
   - Check heatmap generation
   - Download report

### Step 3: Deploy Online (OPTIONAL - 10 minutes)

#### Option A: Streamlit Cloud (Recommended - FREE)

1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `medical-image-analysis`
5. Main file path: `demo/app.py`
6. Click "Deploy"
7. Share the URL: `https://your-app.streamlit.app`

#### Option B: Hugging Face Spaces (FREE)

1. Go to https://huggingface.co/spaces
2. Create new Space
3. Choose Streamlit SDK
4. Upload your files
5. Deploy

### Step 4: Demo Presentation Tips

**What to Show:**
1. ✅ GitHub repository with clean README
2. ✅ Live running application
3. ✅ Upload image and show real-time analysis
4. ✅ Explain the 4 disease classifications
5. ✅ Show confidence scores and visualizations
6. ✅ Demonstrate report generation

**Key Talking Points:**
- "AI-powered chest X-ray analysis system"
- "Uses deep learning (DenseNet architecture)"
- "Classifies 4 conditions: Normal, Pneumonia, COVID-19, TB"
- "Provides confidence scores and attention heatmaps"
- "Generates downloadable clinical reports"
- "Built with modern ML stack: TensorFlow, Streamlit"

**Future Enhancements to Mention:**
- Train on larger medical datasets
- Add DICOM support
- Implement Grad-CAM for better explainability
- Deploy as REST API
- Add user authentication
- Mobile app integration

### Troubleshooting

**Issue: TensorFlow installation fails**
```bash
pip install tensorflow-cpu==2.15.0  # Use CPU version if GPU fails
```

**Issue: Streamlit won't start**
```bash
streamlit run app.py --server.port 8502  # Try different port
```

**Issue: Image upload not working**
- Check file permissions
- Try with a different image format (PNG, JPG)
- Use the "sample image" checkbox instead

### Quick Demo Script

```
"Hello! I've developed an AI-powered Medical Image Analysis system.

[Show GitHub repo]
Here's the repository with full documentation and code.

[Open local app]
The system uses deep learning to analyze chest X-rays.

[Upload image]
I can upload an X-ray image, and within seconds...

[Show results]
...it provides a classification with confidence scores.

It detects 4 conditions: Normal, Pneumonia, COVID-19, and Tuberculosis.

[Show heatmap]
This attention heatmap shows which regions the AI focused on.

[Show report]
And it generates a downloadable clinical report.

Currently using a demo model, but the architecture is ready
for training on real medical datasets for production use.

Thank you!"
```

### Time Breakdown
- GitHub setup: 5 min
- Local testing: 5 min  
- Deploy online: 10 min (optional)
- Practice demo: 5 min
- **Total: 15-25 minutes**

### Emergency Backup
If everything fails, you can:
1. Show the code on GitHub
2. Share screenshots of the running app
3. Walk through the architecture on whiteboard

Good luck with your 3 PM demo! 🚀
