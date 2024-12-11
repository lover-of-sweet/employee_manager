FROM python:3.7

WORKDIR /employee_management

RUN apt update && apt install -y \
    libpq-dev tree

COPY requirements.txt /employee_management/

RUN pip install --no-cache-dir --upgrade -r /employee_management/requirements.txt
