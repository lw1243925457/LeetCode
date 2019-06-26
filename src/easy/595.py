#!/usr/bin/env python
# @Time    : 2019/6/26 17:22
# @Author  : LiuWei
# @Site    : 
# @File    : 595.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
595. Big Countries
Easy

370

523

Favorite

Share
SQL Schema
There is a table World

+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+
A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.

Write a SQL solution to output big countries' name, population and area.

For example, according to the above table, we should output:

+--------------+-------------+--------------+
| name         | population  | area         |
+--------------+-------------+--------------+
| Afghanistan  | 25500100    | 652230       |
| Algeria      | 37100000    | 2381741      |
+--------------+-------------+--------------+

each name(country) can have only one record in this table, so adding distinct on top of the extracted data adds up more
work to the query.

是数据库中国家存在多天记录?一个国家应该只有一条记录把,添不添加distinct应该都是要遍历整个表的吧?性能的提升点事在哪里?
"""
select distinct name, population, area from World where area > 3000000 OR population > 25000000;