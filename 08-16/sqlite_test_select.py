#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":

    connector = sqlite3.connect("sqlite_test.db")
    cursor = connector.cursor()
    cursor.execute("select * from test_table order by code")

    result = cursor.fetchall()

    for row in result:
        print "===== Hit! ====="
        print "code -- " + unicode(row[0])
        print "name -- " + unicode(row[1])

    cursor.close()
    connector.close()

