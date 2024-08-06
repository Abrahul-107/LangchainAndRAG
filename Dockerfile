FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
ENV API_KEY=apikeyplaceholder
# Run the Streamlit app when the container launches
CMD ["streamlit", "run", "App/langchainstreamlit.py"]


