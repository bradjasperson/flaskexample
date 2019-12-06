From python:3.6-alpine

#Expose Flask port
EXPOSE 5000

#Working directory
WORKDIR /app

#Install prerequisites
COPY requirements.txt /app
RUN pip install -r requirements.txt

#Copy scripts in place
COPY app.py /app

#Copy Empty Database
COPY app.sqlite /app

#Start application
CMD python app.py
