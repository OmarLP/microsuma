FROM python:3.12.5-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
# Establece variables de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación
#CMD ["flask", "run"]

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]