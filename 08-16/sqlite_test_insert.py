#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":
    connector = sqlite3.connect("sqlite_test.db")

    sql = "insert into test_table values('1','python')"
    connector.execute(sql)
    sql = "insert into test_table values('2','パイソン')"
    connector.execute(sql)
    sql = "insert into test_table values('3','ぱいそん')"
    connector.execute(sql)

    connector.commit()
    connector.close()

