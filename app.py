from E_data_system import app, db

                                            







if __name__ == "__main__":
    db.create_all()
    # db.drop_all()
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True, port=5000)
    # colors = #243a5e #6093b2 #90dc91 #55b0e2
    # pip install flask-admin
    