FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt 

COPY . .

ENV HISTORICO=/dados/historico.log

RUN mkdir /dados && useradd --create-home appuser && chown appuser /dados

USER appuser

EXPOSE 5000

CMD [ "python3" , "app.py" ]