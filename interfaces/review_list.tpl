<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Review Page</title>
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
    </style>
</head>
<body>
    <header class="header">
        <h1>User Reviews</h1>
    </header>

    <div>
        <!-- Back and Publish Review Button -->
        <a href="/topic_list" class="btn-link" id="BacktoTopics">Back</a>
        <a href="/post_review" class="btn-link" id="publishReviewBtn">Publish Review</a>
    </div>

    <!-- Display Reviews -->
    <div class="reviews"\\>
        <h2>Reviews:</h2>
        <div id="reviewList">
            <!-- Placeholder example reviews(can be removed later) -->
            <div class="review individual">
                <h3>Example-1</h3>
                <p>Random review content blah blah blah </p>
            </div>
            <div class="review group">
                <h3>Example-2</h3>
                <p>Random group review content blah blah blah</p>
            </div>
        </div>
    </div>

</body>
</html>
