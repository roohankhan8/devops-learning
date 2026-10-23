import os
import time

import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

DB_CONFIG = {
    "host": os.environ["DB_HOST"],
    "port": int(os.getenv("DB_PORT", "3306")),
    "database": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.get("/")
def home():
    return jsonify({"message": "Health API is running"})


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/health/db")
def database_health():
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()

        return jsonify({"database": "ok"}), 200

    except mysql.connector.Error:
        app.logger.exception("Database health check failed")
        return jsonify({"database": "unavailable"}), 503

    finally:
        if connection is not None and connection.is_connected():
            connection.close()


@app.get("/time")
def current_time():
    return jsonify({"unix_time": int(time.time())})