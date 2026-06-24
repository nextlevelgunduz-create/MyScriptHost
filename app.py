from flask import Flask, Response

app = Flask(__name__)

# BURA ŞİFRƏLƏDİYİN KODU YAPIŞDIR
SECRET_SCRIPT = """
print("Next Level Hub işə düşdü!")
"""

@app.route('/')
def get_script():
    return Response(SECRET_SCRIPT, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)