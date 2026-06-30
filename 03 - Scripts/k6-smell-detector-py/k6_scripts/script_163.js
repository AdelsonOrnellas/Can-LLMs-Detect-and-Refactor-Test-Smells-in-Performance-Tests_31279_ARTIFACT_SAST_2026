import http from 'k6/http';
import { check, sleep } from 'k6';
//& "C:\ProgramData\chocolatey\bin\k6.exe" run rate-limit-not-breach-test.js
export let options = {
  vus: 1,                // 1 virtual user = 1 IP
  iterations: 10         // Send only 10 requests total
};

let statusCounts = {};

export default function () {
  const payload = JSON.stringify({
    email: 'test@example.com',
    password: 'TestPassword123'
  });

  const headers = {
    'Content-Type': 'application/json'
  };

  const res = http.post('http://localhost:3000/guestUser/logIn', payload, { headers });

  // Accept all expected responses
  check(res, {
    'status is 200/400/401': (r) => [200, 400, 401].includes(r.status),
  });

  // Count status codes
  statusCounts[res.status] = (statusCounts[res.status] || 0) + 1;

  // Sleep for 1.1s to stay above CONSTRAINT_TIME = 1000ms
  sleep(1.1);
}

export function teardown() {
  console.log("✅ Final status code counts:");
  console.log(JSON.stringify(statusCounts, null, 2));
}