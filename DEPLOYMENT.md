# Deployment Guide

## Quick Deploy to Streamlit Cloud (5 minutes)

### Prerequisites
- GitHub account
- Your code pushed to GitHub

### Steps

1. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Click "Sign in with GitHub"

2. **Create New App**
   - Click "New app" button
   - Repository: Select `medical-image-analysis`
   - Branch: `main`
   - Main file path: `demo/app.py`
   - App URL: Choose your custom URL

3. **Deploy**
   - Click "Deploy!"
   - Wait 2-3 minutes for deployment
   - Your app will be live at: `https://your-app-name.streamlit.app`

4. **Share**
   - Copy the URL
   - Share with your demo audience

## Alternative: Local Presentation

If you can't deploy online in time:

1. **Run locally**
   ```bash
   streamlit run demo/app.py
   ```

2. **Share your screen** during the presentation

3. **Use ngrok for temporary public URL** (optional)
   ```bash
   # Install ngrok
   npm install -g ngrok
   
   # Run ngrok
   ngrok http 8501
   
   # Share the ngrok URL
   ```

## Docker Deployment (Advanced)

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "demo/app.py"]
```

Build and run:
```bash
docker build -t medical-image-analysis .
docker run -p 8501:8501 medical-image-analysis
```

## Cloud Deployment Options

### AWS (Elastic Beanstalk)
- Create application
- Upload code
- Configure environment

### Google Cloud (Cloud Run)
- Build container
- Deploy to Cloud Run
- Set up domain

### Heroku
- Install Heroku CLI
- Create `Procfile`:
  ```
  web: streamlit run demo/app.py
  ```
- Deploy:
  ```bash
  heroku create
  git push heroku main
  ```

## Production Considerations

- Add authentication
- Set up logging
- Configure CORS
- Add rate limiting
- Use production WSGI server
- Set up monitoring
- Implement CI/CD pipeline
