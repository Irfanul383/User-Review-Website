...<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Post Review</title>
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

        .rating-container {
            margin-top: 20px;
        }

        .rating-label {
            font-weight: bold;
        }

        .rating-options label {
            display: block;
            cursor: pointer;
            margin-bottom: 10px;
        }

        .rating-options input[type="radio"] {
            display: none;
        }

        .rating-options label:before {
            content: '\25A1';
            font-size: 24px;
            padding-right: 10px;
        }

        .rating-options input[type="radio"]:checked + label:before {
            content: '\2611';
            color: green;
        }
    </style>
</head>
<body>
    <div class="header">
        <a class="btn-link" href="/topic_list" id="BackToReviewlist">Back</a>
    </div>
    <div class="content">
        <h1>Post a Review</h1>
        <form action="/post_review" method="post"> <!-- Updated the form action to the desired endpoint -->
            <!-- Rating Scale -->
            <div class="rating-container">
                <p class="rating-label">How do you rate this question on a scale of 1-10?</p>
                <div class="rating-options">
                    <label for="rating1">
                        What is your overall impression?
                        <input type="number" id="rating1" name="rating1" min="1" max="10" required>
                    </label>
                    <label for="rating2">
                        How well did it meet your expectations?
                        <input type="number" id="rating2" name="rating2" min="1" max="10" required>
                    </label>
                    <label for="rating3">
                        Would you recommend this to others?
                        <input type="number" id="rating3" name="rating3" min="1" max="10" required>
                    </label>
                </div>
            </div>
            <div class="button-container">
                <button type="submit" class="btn-link btn-red">Post Review</button>
                <a href="/write_review" id="WriteReview">Write your own review</a>
            </div>
        </form>
    </div>
</body>
</html>