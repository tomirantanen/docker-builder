FROM python:3-alpine

WORKDIR /app
RUN apk add --no-cache git docker
RUN pip install gitpython docker
COPY . .

ENTRYPOINT [ "python", "./builder.py" ]
