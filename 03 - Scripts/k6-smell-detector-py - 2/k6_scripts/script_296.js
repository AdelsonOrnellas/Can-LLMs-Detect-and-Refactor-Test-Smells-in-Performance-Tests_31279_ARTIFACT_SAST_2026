import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10m', target: 1000000 }, 
  ],
};

export default () => {
    http.get('https://quickpizza.grafana.com/test.k6.io/');
    console.log("test.k6.io")
    sleep(1);
    http.get('https://quickpizza.grafana.com/contacts.php');
    console.log("contacts")
    sleep(2);
    http.get('https://quickpizza.grafana.com/news.php');
    console.log("news")
    sleep(2);
};