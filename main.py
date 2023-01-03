#This is test file for creating a Docker image using Python
FROM python:3.9

ADD test.py

RUN pip install requests beautifulsoup4 python-dotenv

CMD ["python", "./test.py"]



#After executing the script above, enter the following in the terminal
docker run python-imagename
