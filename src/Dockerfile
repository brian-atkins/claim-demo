FROM python:3.11.4-slim

ENV HY_API_PORT=80
EXPOSE $HY_API_PORT

WORKDIR app
COPY claim-processor/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY claim-processor .

CMD ["python", "run.py"]
