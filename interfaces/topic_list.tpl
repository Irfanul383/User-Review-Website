<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Topic Page</title>
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
        .review_filters {
            display: flex;
            column-gap: 10px;
            align-items: center;
        }

        .review {
            margin-bottom: 20px;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
        }

        .btn-link {
            display: inline-block;
            padding: 10px;
            text-decoration: none;
            color: #040404;
            background-color: #c0d2e5;
            border-radius: 5px;
            cursor: pointer;
            margin-right: 10px;
        }
        .btn-red {
            color: white;
            background-color: red;
        }
        topic-box {
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
        .topic-box:hover {
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>User Topic</h1>
        <!-- Logout Button -->
        <a href="/logout" class="btn-link btn-red" id="logoutBtn">Logout</a>
    </header>

    <div class="review_filters">
        <!-- Publish Review Button -->
        <a href="/post_review" class="btn-link" id="publishReviewBtn">New Review</a>
        <!-- Publish Topic Button -->
        <a href="/write_topic" class="btn-link" id="publishTopicBtn">New Topic</a>

        <!-- Toggle for Review Tags -->
        <form action="/get-Topics-by-tags" method="POST">
            <label for="TopicTagToggle">Select Topic Tag:</label>
            <select id="TopicTagToggle" name="Topic_tag" >
                <option value="all">All</option>
            </select>
            <button>Submit</button>
        </form>
    </div>

    <!-- Display Topics -->
    <div class="Topics">
        <h2>Topics:</h2>
        <div id="TopicList">
            <div class="topic-box" onclick="location.href='/review_list'">
                <h3>Example-1</h3>
                <p>Random Topic content blah blah blah</p>
            </div>
            <div class="topic-box" onclick="location.href='/review_list'">
                <h3>Example-2</h3>
                <p>Random Topic content blah blah blah</p>
            </div>
        </div>
    </div>

</body>
</html>