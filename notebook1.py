# Databricks notebook source
# MAGIC %pwd

# COMMAND ----------

# MAGIC %ls

# COMMAND ----------

# MAGIC %%writefile demo1.txt
# MAGIC 
# MAGIC A conflicting update from the data plane.

# COMMAND ----------

!cat demo1.txt
