FROM python:3.7

EXPOSE 8080
WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md

COPY src/ .


CMD ["gunicorn", "wsgi:app", "-w 2", "-b 0.0.0.0:8080", "-t 30"]
