
FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .

ENV FIND=$FIND
ENV UPDATEONE=$UPDATEONE
ENV KEY=$KEY
ENV DELETE=$DELETE
ENV INSERT=$INSERT

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0"]