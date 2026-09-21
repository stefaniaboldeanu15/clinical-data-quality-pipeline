FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY data ./data
ENV PYTHONPATH=/app/src
CMD ["python","-m","quality_pipeline.main","data/sample_clinical_records.csv"]
