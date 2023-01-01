FROM python:latest
ADD sudokuSolver.py /

RUN pip install numpy
CMD ["python", "./sudokuSolver.py"]

