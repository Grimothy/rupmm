const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const cors = require('cors');
const app = express();
const port = 3000; // or 3001, depending on your setup

app.use(cors({
    origin: 'https://rupmm.bearald.com', // Allow requests from your web server
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true,
    optionsSuccessStatus: 204
}));
app.use(bodyParser.json());

app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const embyUrl = 'https://rupemby.bearald.com';
    const apiKey = '509eef1199bc456a9e9ba04a46212f04'; // Your actual API key

    try {
        const response = await axios.post(`${embyUrl}/Users/AuthenticateByName`, {
            Username: username,
            Pw: password
        }, {
            headers: {
                'Content-Type': 'application/json',
                'X-Emby-Authorization': `MediaBrowser Client="YourAppName", Device="YourDeviceName", DeviceId="YourDeviceId", Version="1.0.0.0"`,
                'X-Emby-Token': apiKey
            }
        });

        if (response.data.AccessToken) {
            res.json({ success: true, data: response.data });
        } else {
            res.json({ success: false, message: 'Authentication failed' });
        }
    } catch (error) {
        console.error('Error connecting to Emby server:', error.message);
        res.status(500).json({ success: false, message: 'An error occurred. Please try again later.' });
    }
});

app.listen(port, () => {
    console.log(`Proxy server running at http://localhost:${port}`);
});