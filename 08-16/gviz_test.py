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
    google.load('visualization', '1', {packages: ['annotatedtimeline']});
    </script>
    <script type="text/javascript">
        google.setOnLoadCallback(drawTable);
        google.setOnLoadCallback(drawVisualization);
        google.setOnLoadCallback(drawAnnotatedTimeLine);

        function drawTable() {
            var json_table = new google.visualization.Table(document.getElementById('table_div_json'));
            var json_data = new google.visualization.DataTable(%(json)s, 0.6);
            json_table.draw(json_data, {showRowNumber: true});
        }
        function drawVisualization() {
            var wrapper = new google.visualization.ChartWrapper({
              chartType: 'ColumnChart',
              dataTable: [['', 'Germany', 'USA', 'Brazil', 'Canada', 'France', 'RU'],
                ['', 700, 300, 400, 500, 600, 800]],
              options: {'title': 'Salary'},
              containerId: 'xxx'
            });
            wrapper.draw();
        }
        function drawAnnotatedTimeLine() {
      var data = new google.visualization.DataTable();
      data.addColumn('date', 'Date');
      data.addColumn('number', 'Sold Pencils');
      data.addColumn('string', 'title1');
      data.addColumn('string', 'text1');
      data.addColumn('number', 'Sold Pens');
      data.addColumn('string', 'title2');
      data.addColumn('string', 'text2');
      data.addRows([
        [new Date(2008, 1 ,1), 30000, null, null, 40645, null, null],
        [new Date(2008, 1 ,2), 14045, null, null, 20374, null, null],
        [new Date(2008, 1 ,3), 55022, null, null, 50766, null, null],
        [new Date(2008, 1 ,4), 75284, null, null, 14334, 'Out of Stock', 'Ran out of stock on pens at 4pm'],
        [new Date(2008, 1 ,5), 41476, 'Bought Pens', 'Bought 200k pens', 66467, null, null],
        [new Date(2008, 1 ,6), 33322, null, null, 39463, null, null]
      ]);

      var annotatedtimeline = new google.visualization.AnnotatedTimeLine(
          document.getElementById('visualization'));
      annotatedtimeline.draw(data, {'displayAnnotations': true});

        }
    </script>
    </head>
    <body style="font-family: Arial;border: 0 none;">
        <H1>Table created using ToJSon</H1>
        <div id="table_div_json"></div>
        <div id="xxx" style="width: 600px; height: 400px;"></div>
<div id="visualization" style="width: 800px; height: 400px;"></div>

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
