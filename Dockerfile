FROM python:3.11.1

# ensures that the python output 
# i.e. the stdout and stderr streams are sent straight to terminal 
ENV PYTHONUNBUFFERED 1

ARG DEV=false

COPY requirements.txt /app/
COPY requirements.dev.txt /app/
COPY app /app/

WORKDIR /app
RUN pip install -r requirements.txt

# install this only if it is dev mode
RUN if [ $DEV = true ]; then pip install -r requirements.dev.txt; fi

EXPOSE 8000
