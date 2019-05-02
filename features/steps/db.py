from behave import *
from assertpy import assert_that
import psycopg2
from sshtunnel import SSHTunnelForwarder


@step('I get users from database')
def get_users_from_db(context):
    with SSHTunnelForwarder(
         ('146.185.143.168', 22),
         ssh_password="testQA2019",
         ssh_username="root",
         remote_bind_address=('localhost', 5432)) as server:

        conn = psycopg2.connect(database="mantisbt", port=server.local_bind_port, user='mantisbt', host='localhost', password='mantisbt2019')
        conn.autocommit = True
        curs = conn.cursor()
        try:
            curs.execute("Select username From mantis_user_table;")


        except:
            print("Unable to connect to the database.")
        users = set()
        for row in curs:
            row = row[0].strip(',')
            users.add(row)
        context.users_from_db = users
        conn.close()


@step('I compare userlists')
def compare_userlists(context):
    assert_that(context.users_from_db).is_equal_to(context.users_from_webpage)

