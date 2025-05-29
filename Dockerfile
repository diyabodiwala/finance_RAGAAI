FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["streamlit", "run", "streamlit_app/app.py", "--server.port=10000", "--server.address=0.0.0.0"]

