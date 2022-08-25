FROM python:3.8.10
ENV SECRET_KEY='django-insecure-o#zq!q(sgj7z8snzjhuk3ngo*e7ew83*y^0nk*jidfmd(1&09+'


WORKDIR /test
COPY . /test
COPY ./ticket ./ticket
#RUN pipenv install
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile


CMD [ "python3", "./ticket/manage.py", "runserver", "0.0.0.0:8000"]