FROM python:3.11

EXPOSE 8080

WORKDIR /app

COPY . ./

#ENV GOOGLE_APPLICATION_CREDENTIALS=""
ENV GOOGLE_CLOUD_PROJECT="Hera"
ENV GCP_PROJECT_NAME="Hera"

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080"]