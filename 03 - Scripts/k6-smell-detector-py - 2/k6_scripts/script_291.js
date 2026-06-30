import http from 'k6/http';
import { check } from 'k6';

const payload = JSON.stringify({
  meta: {
    user_id: "b66adzazdazdazdazd7bd06-2753-44ae-adazd8848f60-26df8d351d0f",
    resource_id: "b66adzazdazdazdazd7bd06-2753-44ae-adazd8848f60-26df8d351d0f",
    status: "pos",
  },
  webhook_meta: {
    client_id: "hello-this-is-aclient-id",
    webhook_config_id: "config-id",
    webhook_msg_timestamp: 1729651095,
    webhook_msg_uuid: "b66adzazdazdazdazd7bd06-2753-44ae-adazd8848f60-26df8d351d0f",
  },
});

const headers = {
  "Content-Type": "application/json",
};

export const options = {
  vus: 10,
  duration: "30s",
};

export default function () {
  const res = http.post("http://localhost:3000/api", payload, { headers });
  check(res, { "status is 200": (r) => r.status === 200 });
}

