FROM python:3.10-slim
WORKDIR /app
COPY linear_regression.py .
RUN pip install numpy scikit-learn
CMD ["python", "linear_regression.py"]