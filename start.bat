@echo off
REM Quick Start Script for Medical Image Analysis Demo (Windows)

echo 🏥 Medical Image Analysis - Quick Start
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo ✅ Python found

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo 📥 Installing dependencies (this may take a few minutes)...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Run the app
echo 🚀 Starting application...
echo.
echo The app will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

cd demo
streamlit run app.py

pause
