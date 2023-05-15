FROM python:3.11-alpine
ENV TOKEN=default_token_value
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /app
CMD ["python", "main.py"]
