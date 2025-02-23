const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const embyUrl = 'https://rupemby.bearald.com';
    const apiKey = '509eef1199bc456a9e9ba04a46212f04'; // Replace with your actual API key

    try {
        const response = await axios.post(`${embyUrl}/Users/AuthenticateByName`, {
            Username: username,
            Pw: password
        }, {
            headers: {
                'Content-Type': 'application/json',
                'X-Emby-Authorization': `MediaBrowser Client="YourAppName", Device="YourDeviceName", DeviceId="YourDeviceId", Version="1.0.0.0"`,
                'X-Emby-Token': apiKey // Add the API key here
            }
        });

        if (response.data.AccessToken) {
            res.json({ success: true, data: response.data });
        } else {
            res.json({ success: false, message: 'Authentication failed' });
        }
    } catch (error) {
        res.status(500).json({ success: false, message: 'An error occurred. We seem to be having issues connecting to the backend API. Please try again later.', error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});