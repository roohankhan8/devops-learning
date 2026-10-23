import os
import unittest

# Provide test configuration without requiring a running database.
os.environ.setdefault("DB_HOST", "db")
os.environ.setdefault("DB_PORT", "3306")
os.environ.setdefault("DB_NAME", "appdb")
os.environ.setdefault("DB_USER", "appuser")
os.environ.setdefault("DB_PASSWORD", "test-password")

from app import app


class HealthApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"message": "Health API is running"},
        )

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_time_endpoint(self):
        response = self.client.get("/time")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json()["unix_time"], int)


if __name__ == "__main__":
    unittest.main()
