FROM python
RUN pip install fastapi uvicorn
COPY main.py main.py
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]

