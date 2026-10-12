from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Cloud DevOps Starter</title>
        <style>
          :root { color-scheme: light; --blue: #003da1; }
          body { margin: 0; font-family: Arial, sans-serif; background: #f3f7ff; color: #152238; }
          main { max-width: 760px; margin: 10vh auto; padding: 36px; background: white;
                 border: 1px solid #d8e4ff; border-radius: 18px; box-shadow: 0 12px 35px #003da11a; }
          h1 { color: var(--blue); margin-top: 0; }
          .pill { display: inline-block; padding: 7px 12px; border-radius: 999px;
                  background: #e6eeff; color: var(--blue); font-size: 14px; }
          a { color: var(--blue); }
        </style>
      </head>
      <body>
        <main>
          <span class="pill">Cloud & DevOps Portfolio Project</span>
          <h1>It works!</h1>
          <p>This Flask application is running. The next step is to package it with Docker
             and use GitHub Actions to run an automated test on every push.</p>
          <p><a href="/health">Check application health</a></p>
        </main>
      </body>
    </html>
    """

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
