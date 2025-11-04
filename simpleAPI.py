from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# -----------------------------
# Helper function: DB connection
# -----------------------------
def get_db_connection():
    conn = mysql.connector.connect(
        host='db.cwiztech.com',
        port='3348',
        user='root',
        password='ALLAH',
        database='fyp'
    )
    return conn

# -----------------------------
# Routes
# -----------------------------

@app.route('/')
def home():
    return jsonify({'message': 'Flask API is running!'})

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    
    # ✅ Use dictionary=True so results come as dicts
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM tbluser")
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # ✅ results is now a list of dicts — safe to jsonify
    return jsonify(results)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM tbluser WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()  # fetch one record
    
    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()

    # ✅ Use %s placeholders, not ?
    query = "INSERT INTO tbluser (USER_NAME, EMAIL) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': 'User added successfully!'}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()

    # ✅ Use %s placeholders, not ?
    query = "update tbluser set USER_NAME=%s, EMAIL=%s where USER_ID=%s"
    cursor.execute(query, (name, email, user_id))
    
    conn.commit()
    affected = cursor.rowcount  # number of rows updated
    
    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User updated successfully!'}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM tbluser WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()

    affected = cursor.rowcount  # number of rows deleted

    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User deleted successfully!'}), 200

# -----------------------------
# Run the app
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5001)