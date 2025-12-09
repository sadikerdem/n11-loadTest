from locust import HttpUser, task, between

class N11User(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.client.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
            "Accept": "text/html",
        }

    @task
    def search_iphone(self):
        self.client.get("/")
        self.client.get("/arama?q=iphone")
