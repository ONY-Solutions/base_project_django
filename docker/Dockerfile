FROM python:3.12-alpine AS build
WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache/pip


FROM python:3.12-alpine

COPY --from=build /app /app

WORKDIR /app
COPY ./ /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "config.server.wsgi:application"]