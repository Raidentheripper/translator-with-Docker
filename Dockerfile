
FROM python:3.11-slim

LABEL description="Translator app — googletrans lab work"

WORKDIR /Horodynets

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY translator.py .

CMD ["python", "translator.py"]
