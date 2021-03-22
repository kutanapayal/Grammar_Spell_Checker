FROM python:3.6
WORKDIR /usr/src/app
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3","./test.py"]
#CMD ["uvicorn", "app.main:app", "--host", "ec2-3-84-239-94.compute-1.amazonaws.com", "--port", "80"]