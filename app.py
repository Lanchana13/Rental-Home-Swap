from flask import Flask, render_template, url_for, request
import sqlite3
import json
import os

connection = sqlite3.connect('Database.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS admin(name TEXT, password TEXT)"""
cursor.execute(command)

name='admin'
password='admin@123'
cursor.execute("INSERT INTO admin VALUES ('"+name+"', '"+password+"')")
connection.commit()
