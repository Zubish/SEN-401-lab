FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python", "lab4/controllers.py"]