#!/usr/bin/env python

import gviz_api
import flask

APP = flask.Flask(__name__)

page_template = """
<html>
    <head>
    <script src="https://www.google.com/jsapi" type="text/javascript"></script>
    <script>
        google.load('visualization', '1', {packages:['table']});

        google.setOnLoadCallback(drawTable);
        function drawTable() {
            %(jscode)s
            var jscode_table = new google.visualization.Table(document.getElementById('table_div_jscode'));

            var json_table = new google.visualization.Table(document.getElementById('table_div_json'));
            var json_data = new google.visualization.DataTable(%(json)s, 0.6);
            json_table.draw(json_data, {showRowNumber: true});
        }
    </script>
    </head>
    <body>
        <H1>Table created using ToJSCode</H1>
        <div id="table_div_jscode"></div>
        <H1>Table created using ToJSon</H1>
        <div id="table_div_json"></div>
    </body>
</html>
"""


def main():
    # Creating the data
    description = {"name": ("string", "Name"),
                    "salary": ("number", "Salary"),
                    "full_time": ("boolean", "Full Time Employee")}
    data = [{"name": "Mike", "salary": (10000, "$10,000"), "full_time": True},
            {"name": "Jim", "salary": (800, "$800"), "full_time": False},
            {"name": "Alice", "salary": (12500, "$12,500"), "full_time": True},
            {"name": "Bob", "salary": (7000, "$7,000"), "full_time": True}]

    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Creating a JavaScript code string
    jscode = data_table.ToJSCode("jscode_data",
                                    columns_order = ("name", "salary", "full_time"),
                                    order_by = "salary")

    # Creating a JSon string
    json = data_table.ToJSon(columns_order=("name", "salary", "full_time"),
                                order_by = "salary")

    # Putting the JS code and JSon string into the template
    f = open('./templates/index.html', 'w')
    #f.write("Content-type: text/html\n")
    #f.write("\n")
    f.write( page_template % vars() )
    f.close()

    #print "Content-type: text/html"
    #print
    #print page_template % vars()

@APP.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    main()
    APP.debug = True
    APP.run(port=8000)

