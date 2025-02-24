<?php
// filepath: /var/www/html/rupmm/login.php

// Start output buffering
ob_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $url = 'https://rupemby.bearald.com/Users/AuthenticateByName';
    $apiKey = '509eef1199bc456a9e9ba04a46212f04'; // Your actual API key

    $data = array(
        'Username' => $username,
        'Pw' => $password
    );

    $options = array(
        'http' => array(
            'header'  => "Content-Type: application/json\r\n" .
                         "X-Emby-Authorization: MediaBrowser Client=\"YourAppName\", Device=\"YourDeviceName\", DeviceId=\"YourDeviceId\", Version=\"1.0.0.0\"\r\n" .
                         "X-Emby-Token: $apiKey\r\n",
            'method'  => 'POST',
            'content' => json_encode($data),
        ),
    );

    $context  = stream_context_create($options);
    $result = file_get_contents($url, false, $context);

    if ($result === FALSE) {
        // Handle error
        echo 'An error occurred. Please try again later.';
    } else {
        $response = json_decode($result, true);
        if (isset($response['AccessToken'])) {
            // Authentication successful
            header('Location: welcome.html'); // Redirect to welcome page
            exit();
        } else {
            // Authentication failed
            echo 'Login failed. Please check your username and password.';
        }
    }
} else {
    echo 'Invalid request method.';
}

// End output buffering and flush output
ob_end_flush();
?>