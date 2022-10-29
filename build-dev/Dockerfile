FROM python:3.10
LABEL maintainer "João Godoi <joaogodoi.dev@gmail.com>"

RUN useradd admin && \
    mkdir /app && \
    mkdir /log && \
    chown admin /log

USER admin
VOLUME /log
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["run.py"]
