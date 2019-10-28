FROM python:3.6.2

RUN pip3 install pyyaml pytz numpy six
RUN pip3 install django

RUN mkdir /titanGUI
WORKDIR /titanGUI
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]
EXPOSE 8000
