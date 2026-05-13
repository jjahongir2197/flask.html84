<!DOCTYPE html>
<html>
<head>
    <title>Upload Images</title>
</head>
<body>

    <h1>Image Upload</h1>

    <form method="POST" enctype="multipart/form-data">

        <input type="file" name="file">
        <button>Upload</button>

    </form>

    <hr>

    {% for img in images %}

        <img src="{{ img }}" width="200">
        <hr>

    {% endfor %}

</body>
</html>
