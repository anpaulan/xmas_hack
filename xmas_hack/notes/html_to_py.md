from flask import request

@app.route('/addRegion', methods=['POST'])
def addRegion():
    ...
    return (request.form['projectFilePath'])
   
<form action="{{ url_for('addRegion') }}" method="post">
    Project file path: <input type="text" name="projectFilePath"><br>
    <input type="submit" value="Submit">
</form>