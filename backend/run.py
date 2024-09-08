from app import create_app

app = create_app()

if __name__ == "__main__":
      app.run(debug=True, host='local_host', port=8080)

# from flask import Flask

# def create_app():
#     app = Flask(__name__)

#     #Import routes from the route module
    

#     return app