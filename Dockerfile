FROM python:3.14-slim

WORKDIR /workspace

COPY requirment.txt .
RUN pip install --no-cache-dir -r requirment.txt

COPY . .

RUN python train.py

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]