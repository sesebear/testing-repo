FROM python:3.12.0

WORKDIR /test
ADD test.py .
CMD [ "python", "./test.py"]