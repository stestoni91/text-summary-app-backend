FROM python:3.9

RUN useradd -m -u 1000 user

WORKDIR /appz

COPY --chown=user ./requirements.txt requirements.txt
# COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN pip install -r requirements.txt

COPY --chown=user . /appz
# COPY . /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]