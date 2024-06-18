FROM python:3.9
WORKDIR /usr/app
COPY . .
RUN pip install -r requirements.txt
CMD ["python","app.py"]
EXPOSE 5000