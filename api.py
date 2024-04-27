import mysql.connector
from flask import Blueprint
from flask import jsonify

application = Blueprint('api', __name__)
# Configuration for MySQL database
db_config = {
    'host': 'host.docker.internal',
    'user': 'root',
    'password': 'my-secret-pw',
    'database': 'yasas_db'
}


# Function to fetch data from the Github table
def fetch_github_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT language_name, year, quarter, total_issue_count, total_prs_count, total_repo_count FROM Github")
        github_data = cursor.fetchall()
        return github_data
    except Exception as e:
        print("Error:", e)
    finally:
        if 'connection' in locals():
            connection.close()


# Example route to display Github data
@application.route('/getdata')
def get_github_data():

    github_data = fetch_github_data()
    if github_data:
        json_data = [{
            'language_name': row[0],
            'year': row[1],
            'quarter': row[2],
            'total_issue_count': row[3],
            'total_prs_count': row[4],
            'total_repo_count': row[5]
        } for row in github_data]
        return jsonify(json_data)
    else:
        return jsonify({"message": "No data found.!"})
