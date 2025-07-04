FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

RUN apt-get install -y supervisor
# RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY overlays/supervisor/app /app

# webdav
RUN cd wsgidav && uv pip install --system -r requirements.txt
RUN mkdir /webdav

# supervisor
RUN mv /etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf.backup
COPY overlays/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY overlays/supervisor/conf.d /etc/supervisor/conf.d

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
