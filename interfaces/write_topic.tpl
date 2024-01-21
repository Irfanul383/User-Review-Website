<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Write Topic</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .btn-link {
            display: inline-block;
            padding: 10px;
            text-decoration: none;
            color: #040404;
            background-color: #c0d2e5;
            border-radius: 5px;
            cursor: pointer;
        }

        .btn-red {
            color: white;
            background-color: red;
        }

        .content {
            margin-top: 20px;
        }

        .text-area {
            width: 1000px;
            height: 50px;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
        }

        .button-container {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="header">
        <a class="btn-link" href="/topic_list" id="BackToTopiclist">Back</a>
    </div>
    <div class="content">
        <h1>Write a Topic</h1>
        <form action="/write_topic" method="post">
            <!-- Area to write Topic -->
            <textarea class="text-area" name="topicContent" placeholder="Write your topic here..." required></textarea>

            <!-- Text Areas for Questions -->
            <p>Question 1:</p>
            <textarea class="text-area" name="question1" placeholder="Enter your first question..." required></textarea>

            <p>Question 2:</p>
            <textarea class="text-area" name="question2" placeholder="Enter your second question..." required></textarea>

            <p>Question 3:</p>
            <textarea class="text-area" name="question3" placeholder="Enter your third question..." required></textarea>

            <!-- Toggle for Topic Tags -->
            <label for="TopicTagToggle">Select Topic Tag:</label>
            <select id="TopicTagToggle" name="Topic_tag" >
                <option value="all">All</option>
                <!-- Add more topic tag options here -->
            </select>

            <div class="button-container">
                <button type="submit" class="btn-link btn-red">Post Topic</button>
            </div>
        </form>
    </div>
</body>
</html>