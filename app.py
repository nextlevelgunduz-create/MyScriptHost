import os
import subprocess

# Flask kitabxanasının yüklü olub-olmadığını yoxlayırıq
try:
    from flask import Flask, Response
except ImportError:
    # Yüklü deyilsə, avtomatik yükləyirik
    subprocess.check_call(["pip", "install", "flask", "gunicorn"])
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
    # Render-in verdiyi portu istifadə edirik
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
