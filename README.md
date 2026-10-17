<div align="center">

# 🐘 PostgreSQL & SQL Practice

**SQL from SELECT to JOINs on the DVD Rental sample database, plus running queries from Python with psycopg2**

<p>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

</div>

---

## 📌 Overview

My notes, exercises and reference material for refreshing **SQL with PostgreSQL**, including how to connect to a database and run queries directly from Python with **psycopg2**.

## 🧭 What's inside

| Topic | Covered |
|---|---|
| Querying | `SELECT`, `DISTINCT`, `WHERE`, `ORDER BY`, `LIMIT`, `BETWEEN`, `IN`, `LIKE` |
| Aggregation | `COUNT`, `SUM`, `AVG`, `MIN/MAX`, `GROUP BY`, `HAVING` |
| Joins | `INNER`, `LEFT/RIGHT`, `FULL OUTER` joins and self joins (`JOIN.pptx`) |
| Advanced | Subqueries, `CASE` expressions, timestamps, views |
| Databases | Creating tables, constraints, `INSERT`, `UPDATE`, `DELETE` |
| Python | Connecting with psycopg2, cursors, `fetchone/fetchmany/fetchall`, dynamic queries |

## 🗄️ Sample database

`dvdrental.tar` is the standard **DVD Rental** sample database (films, actors, customers, rentals, payments). Its schema is in `Database-Schema.png`.

## 📂 Repository structure

```
├── dvdrental.tar           # DVD Rental sample database (restore with pg_restore)
├── exercises.tar           # practice database for the exercises
├── Database-Schema.png     # schema diagram
├── Pgsql-with-Python.py    # tutorial: running PostgreSQL queries from Python
├── main.py                 # minimal psycopg2 example
├── JOIN.pptx               # visual guide to SQL joins
├── Sql_notes.pdf · notes.docx   # my study notes
└── README.md
```

## 🚀 Getting started

```bash
git clone https://github.com/hamidghasemi69/PostgreSQL.git
cd PostgreSQL

# Restore the sample database
createdb dvdrental
pg_restore -U postgres -d dvdrental dvdrental.tar

# Query it from Python
pip install psycopg2-binary
python main.py      # edit the connection settings first
```

> Keep database passwords out of the code: read them from an environment variable, for example `os.environ["PGPASSWORD"]`.

## 👤 Author

**Hamidreza Ghasemi** · Principal Data Scientist @ Arizona State University

[![Website](https://img.shields.io/badge/Website-hamidghasemi69.github.io-2ee6c5?style=flat-square&logo=googlechrome&logoColor=white)](https://hamidghasemi69.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-hamidghasemi69-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hamidghasemi69/)
[![GitHub](https://img.shields.io/badge/GitHub-hamidghasemi69-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hamidghasemi69)

<sub>If you find this project useful, consider giving it a ⭐</sub>
