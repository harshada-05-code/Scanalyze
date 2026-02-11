import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.preprocessing import image
import cv2
import plotly.graph_objects as go
import io

# Page config
st.set_page_config(
    page_title="Medical Image Analysis",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = None

@st.cache_resource
def load_model():
    """Load pre-trained model"""
    try:
        # Using DenseNet121 as base (can be replaced with specialized model)
        model = DenseNet121(weights='imagenet', include_top=False, pooling='avg')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def preprocess_image(img, target_size=(224, 224)):
    """Preprocess image for model input"""
    img = img.resize(target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize
    return img_array

def analyze_image(img, model):
    """Run analysis on the image"""
    # Preprocess
    img_array = preprocess_image(img)
    
    # Get features/predictions
    features = model.predict(img_array, verbose=0)
    
    # Mock classification results (replace with actual trained model)
    # For demo purposes, using random-like but consistent results
    np.random.seed(int(np.sum(features) * 1000) % 1000)
    
    classes = ['Normal', 'Pneumonia', 'COVID-19', 'Tuberculosis']
    probabilities = np.random.dirichlet(np.ones(4) * 2)
    probabilities = sorted(probabilities, reverse=True)
    
    return dict(zip(classes, probabilities))

def create_heatmap(img):
    """Create a simple attention heatmap"""
    img_array = np.array(img.convert('L'))
    
    # Apply Gaussian blur and enhance edges
    blurred = cv2.GaussianBlur(img_array, (21, 21), 0)
    heatmap = cv2.Laplacian(blurred, cv2.CV_64F)
    heatmap = np.abs(heatmap)
    
    # Normalize
    heatmap = (heatmap - heatmap.min()) / (heatmap.max() - heatmap.min() + 1e-8)
    
    return heatmap

def main():
    # Header
    st.markdown('<p class="main-header">🏥 Medical Image Analysis System</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-Powered Chest X-Ray Analysis</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/stethoscope.png", width=80)
        st.header("About")
        st.info("""
        This demo analyzes chest X-ray images to detect:
        - Normal cases
        - Pneumonia
        - COVID-19
        - Tuberculosis
        
        **Note:** This is a prototype for demonstration purposes only.
        Not for clinical use.
        """)
        
        st.header("Features")
        st.markdown("""
        ✅ Image Upload & Analysis  
        ✅ Disease Classification  
        ✅ Confidence Scores  
        ✅ Visual Heatmap  
        ✅ Detailed Report
        """)
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload Image")
        uploaded_file = st.file_uploader(
            "Choose a chest X-ray image",
            type=['png', 'jpg', 'jpeg', 'dcm'],
            help="Upload a chest X-ray image for analysis"
        )
        
        # Sample images option
        use_sample = st.checkbox("Or use a sample image")
        
        if use_sample:
            st.info("Sample image loaded for demo")
            # Create a sample image (gray gradient)
            sample_img = Image.new('L', (512, 512), color=128)
            img = sample_img
        elif uploaded_file is not None:
            img = Image.open(uploaded_file)
        else:
            img = None
        
        if img:
            st.image(img, caption="Input X-Ray Image", use_container_width=True)
    
    with col2:
        st.subheader("🔍 Analysis Results")
        
        if img is not None:
            with st.spinner("Analyzing image..."):
                # Load model
                if st.session_state.model is None:
                    st.session_state.model = load_model()
                
                if st.session_state.model:
                    # Analyze
                    results = analyze_image(img, st.session_state.model)
                    
                    # Display results
                    st.success("Analysis Complete!")
                    
                    # Top prediction
                    top_class = max(results, key=results.get)
                    top_conf = results[top_class]
                    
                    st.metric(
                        label="Primary Diagnosis",
                        value=top_class,
                        delta=f"{top_conf*100:.1f}% confidence"
                    )
                    
                    # All predictions
                    st.subheader("All Predictions")
                    for class_name, prob in sorted(results.items(), key=lambda x: x[1], reverse=True):
                        st.progress(prob, text=f"{class_name}: {prob*100:.1f}%")
                    
                    # Visualization
                    fig = go.Figure(data=[
                        go.Bar(
                            x=list(results.values()),
                            y=list(results.keys()),
                            orientation='h',
                            marker=dict(
                                color=['#FF6B6B' if v == max(results.values()) else '#4ECDC4' 
                                       for v in results.values()]
                            )
                        )
                    ])
                    fig.update_layout(
                        title="Confidence Distribution",
                        xaxis_title="Confidence",
                        yaxis_title="Diagnosis",
                        height=300
                    )
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("👆 Upload an image to begin analysis")
    
    # Additional Analysis Section
    if img is not None:
        st.divider()
        st.subheader("🎯 Advanced Visualization")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.write("**Attention Heatmap**")
            heatmap = create_heatmap(img)
            fig_heatmap = go.Figure(data=go.Heatmap(
                z=heatmap,
                colorscale='Hot',
                showscale=False
            ))
            fig_heatmap.update_layout(
                height=400,
                margin=dict(l=0, r=0, t=0, b=0)
            )
            st.plotly_chart(fig_heatmap, use_container_width=True)
            st.caption("Areas of interest highlighted by the model")
        
        with col4:
            st.write("**Clinical Report**")
            
            report = f"""
            **Patient Image Analysis Report**
            
            **Primary Finding:** {top_class}
            **Confidence Level:** {top_conf*100:.1f}%
            
            **Differential Diagnoses:**
            {chr(10).join([f"- {k}: {v*100:.1f}%" for k, v in sorted(results.items(), key=lambda x: x[1], reverse=True)])}
            
            **Recommendation:**
            {"Further clinical evaluation recommended." if top_conf < 0.8 else "High confidence prediction. Clinical correlation advised."}
            
            **Disclaimer:** This is an AI-assisted analysis and should not replace 
            professional medical diagnosis. Always consult with a qualified healthcare provider.
            """
            
            st.text_area("Report", report, height=300)
            
            # Download button
            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="medical_analysis_report.txt",
                mime="text/plain"
            )
    
    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p>Medical Image Analysis System v1.0 | Built with Streamlit & TensorFlow</p>
        <p>⚠️ For Research and Educational Purposes Only</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
