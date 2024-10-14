FROM python:3.7.2-alpine3.8
MAINTAINER jmp "jmp@iutbeziers.fr"

RUN apk  update && apk  upgrade && mkdir /app
COPY app.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py  
ENV FLASK_ENV=development
ENTRYPOINT ["flask"]
CMD ["run","--host=0.0.0.0"]
