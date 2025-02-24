#!/bin/bash
# Start your Node.js applications using pm2
pm2 start /var/www/html/proxy-server.js
pm2 start /var/www/html/jelly-proxy.js
pm2-runtime start /var/www/html/proxy-server.js /var/www/html/jelly-proxy.js
