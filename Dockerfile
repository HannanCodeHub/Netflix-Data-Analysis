FROM python:3.12

WORKDIR /app

COPY requirents.txt .

RUN pip install -r requirents.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]