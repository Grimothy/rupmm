#!/bin/bash
pm2 start /var/www/html/proxy-server.js
pm2 start /var/www/html/jelly-proxy.js
pm2-runtime start
