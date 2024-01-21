<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Write Review</title>
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
            height: 200px;
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
        <a class="btn-link" href="/post_review" id="BackToReviewlist">Back</a>
    </div>
    <div class="content">
        <h1>Write a Review</h1>
        <form action="/write_review" method="post"> <!-- Form tag with action and method -->
            <!-- Area to write Review -->
            <textarea class="text-area" name="reviewContent" placeholder="Write your review here..." required></textarea>
            <!-- Checkbox to select "Post as Anonymous" -->
            <div class="checkbox-container">
                <label class="checkbox-label">
                    <input type="checkbox" id="anonymous" name="anonymous"> Post as Anonymous
                </label>
            </div>
            <div class="button-container">
                <!-- Button to submit the form -->
                <button type="submit" class="btn-link btn-red">Post Review</button>
            </div>
        </form>
    </div>
</body>
</html>