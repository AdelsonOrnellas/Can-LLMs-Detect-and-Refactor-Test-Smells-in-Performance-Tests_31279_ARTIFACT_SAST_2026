import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

// Custom metrics
const errorRate = new Rate('errors');

// Test configuration
export const options = {
  stages: [
    { duration: '1m', target: 10 },  // Ramp up to 10 VUs over 1 minute
    { duration: '3m', target: 10 },  // Stay at 10 VUs for 3 minutes
    { duration: '1m', target: 0 },   // Ramp down to 0 VUs over 1 minute
  ],
  thresholds: {
    http_req_duration: ['p(95)<5000'], // 95% of requests should be below 5s
    http_req_failed: ['rate<0.1'],     // Error rate should be below 10%
    errors: ['rate<0.1'],              // Custom error rate should be below 10%
  },
};

// Base URL (will be overridden by environment or command line)
const BASE_URL = __ENV.BASE_URL || 'http://orders-api:3000';

// Sample products for orders
const PRODUCTS = [
  { productId: 'laptop-1', quantity: 1, price: 1299.99 },
  { productId: 'mouse-1', quantity: 2, price: 79.99 },
  { productId: 'keyboard-1', quantity: 1, price: 149.99 },
  { productId: 'monitor-1', quantity: 1, price: 499.99 },
  { productId: 'headset-1', quantity: 1, price: 199.99 },
  { productId: 'chair-1', quantity: 1, price: 299.99 },
];

// Payment methods
const PAYMENT_METHODS = ['credit_card', 'debit_card', 'pix'];

// Generate random customer ID
function randomCustomerId() {
  return `customer_${Math.random().toString(36).substr(2, 9)}`;
}

// Generate random order
function generateRandomOrder() {
  const numItems = Math.floor(Math.random() * 3) + 1; // 1-3 items
  const selectedProducts = [];
  
  for (let i = 0; i < numItems; i++) {
    const product = PRODUCTS[Math.floor(Math.random() * PRODUCTS.length)];
    selectedProducts.push({
      productId: product.productId,
      price: product.price,
      quantity: Math.floor(Math.random() * 3) + 1 // 1-3 quantity
    });
  }
  
  return {
    customerId: randomCustomerId(),
    items: selectedProducts,
    paymentMethod: PAYMENT_METHODS[Math.floor(Math.random() * PAYMENT_METHODS.length)]
  };
}

export default function () {
  // Health check first
  let response = http.get(`${BASE_URL}/health`);
  let healthCheckPassed = check(response, {
    'health check status is 200': (r) => r.status === 200,
    'health check response time < 500ms': (r) => r.timings.duration < 500,
  });
  
  if (!healthCheckPassed) {
    errorRate.add(1);
    sleep(1);
    return;
  }

  // Generate and create order
  const order = generateRandomOrder();
  
  response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
    headers: {
      'Content-Type': 'application/json',
    },
  });

  const orderSuccess = check(response, {
    'order creation status is 201 or 422': (r) => r.status === 201 || r.status === 422,
    'order creation response time < 10s': (r) => r.timings.duration < 10000,
    'response has valid JSON': (r) => {
      try {
        JSON.parse(r.body);
        return true;
      } catch (e) {
        return false;
      }
    },
  });

  if (!orderSuccess) {
    errorRate.add(1);
  }

  // Log order result for debugging
  if (__ENV.VERBOSE === '1') {
    console.log(`Order ${order.customerId}: ${response.status} - ${response.body.substring(0, 100)}`);
  }

  // Wait between requests (simulate user think time)
  sleep(Math.random() * 3 + 1); // 1-4 seconds
}
