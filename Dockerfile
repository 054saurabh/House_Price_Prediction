FROM python:3.10.6

WORKDIR /app-cicd

COPY . /app-cicd

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]

# ENTRYPOINT ["python"]
# CMD  ["app.py"]
