<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        User Registration Page
    </title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            input {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
            }
            form {
                max-width: 300px;
                margin: 0 auto;
            }
            label {
                display: block;
                margin-bottom: 10px;
            }
            .btn {
                display: inline-block;
                padding: 10px;
                text-decoration: none;
                color: #040404;
                background-color: #c0d2e5;
                border-radius: 5px;
                margin-right: 10px;
                cursor: pointer;
            }
        </style>
</head>

<body>
    <h1>
        User Registration Page
    </h1>
        <form action="/register" method="POST">
            <label for="wanted_username">
                Wanted Username:
            </label>
            <input type="text" id="wanted_username" name="wanted_username" required>

            <label for="wanted_password">
                Wanted Password:
            </label>
            <input type="password" id="wanted_password" name="wanted_password" required>
            % if has_error and error_message:
                <div style="color: red; margin-bottom: 10px;">{{error_message}}</div>
            % else:
                 <div style="color: green; margin-bottom: 10px;">Please enter your credentials.</div>
            % end
            <!-- Register Button -->
            <button class="btn">Register</button>
            <br />
            <br />
            Already have an account? <a href="/login">login<a/>
        </form>
</body>
</html>