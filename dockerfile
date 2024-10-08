FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
CMD ["sh", "/code/entrypoint.sh"]