from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

base_html = """
<!DOCTYPE html>
<html>
<head>
    <title>For Ruhi Di</title>
    <style>
        body {{
            background: linear-gradient(to right, #fbc2eb, #a6c1ee);
            font-family: 'Verdana', sans-serif;
            text-align: center;
            color: #2c3e50;
            transition: all 0.8s ease;
        }}
        .container {{
            margin-top: 12%;
            animation: fadeIn 2s ease;
        }}
        h1 {{ font-size: 2.5em; margin-bottom: 20px; }}
        p {{ font-size: 1.2em; margin-bottom: 30px; }}
        a, button {{
            background: #6a82fb;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 25px;
            text-decoration: none;
            font-size: 1.1em;
            transition: 0.3s;
        }}
        a:hover, button:hover {{
            background: #fc5c7d;
            transform: scale(1.05);
        }}
        @keyframes fadeIn {{ from {{opacity: 0;}} to {{opacity: 1;}} }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def chapter1():
    content = """
    <h1>🌸 How It Began 🌸</h1>
    <p>Ruhi di, one year ago Instagram gave me the best gift—you.</p>
    <a href="/chapter2">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter2", response_class=HTMLResponse)
async def chapter2():
    content = """
    <h1>💫 First Conversations 💫</h1>
    <p>Those first chats were filled with warmth and laughter. 
    I knew instantly you were special.</p>
    <a href="/chapter3">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter3", response_class=HTMLResponse)
async def chapter3():
    content = """
    <h1>🌼 Growing Bond 🌼</h1>
    <p>From casual talks to deep conversations, our bond grew stronger every day.</p>
    <a href="/chapter4">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter4", response_class=HTMLResponse)
async def chapter4():
    content = """
    <h1>🎶 Shared Moments 🎶</h1>
    <p>Every laugh, every memory, every inside joke is a treasure I’ll always keep.</p>
    <a href="/chapter5">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter5", response_class=HTMLResponse)
async def chapter5():
    content = """
    <h1>💎 What You Mean 💎</h1>
    <p>You’re more than a friend I met online—you’re my sister, my guide, my forever bond.</p>
    <a href="/chapter6">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter6", response_class=HTMLResponse)
async def chapter6():
    content = """
    <h1>🌹 One Year Together 🌹</h1>
    <p>365 days of love, laughter, and support. This milestone means the world to me.</p>
    <a href="/chapter7">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter7", response_class=HTMLResponse)
async def chapter7():
    content = """
    <h1>❤️ Forever Bond ❤️</h1>
    <p>No matter where life takes us, you’ll always be my Ruhi di, my guiding star.</p>
    <a href="/final">Final Chapter ➝</a>
    """
    return base_html.format(content=content)

@app.get("/final", response_class=HTMLResponse)
async def final_get():
    content = """
    <h1>🔒 Secret Message 🔒</h1>
    <p>Enter the key to unlock my heartfelt words:</p>
    <form method="POST">
        <input type="password" name="password" placeholder="Enter password">
        <button type="submit">Unlock</button>
    </form>
    """
    return base_html.format(content=content)

@app.post("/final", response_class=HTMLResponse)
async def final_post(password: str = Form(...)):
    if password == "250325":  # You can set this to the date you met
        content = """
        <h1>🌹 Ruhi Di, You’re Irreplaceable 🌹</h1>
        <p>One year ago, Instagram gave me the best gift—YOU. 
        You’ll always be my sister, my mentor, and my forever bond.</p>
        """
    else:
        content = """
        <h1>🔒 Secret Message 🔒</h1>
        <p>Enter the key to unlock my heartfelt words:</p>
        <form method="POST">
            <input type="password" name="password" placeholder="Enter password">
            <button type="submit">Unlock</button>
        </form>
        <p style="color:red;">Wrong password, try again.</p>
        """
    return base_html.format(content=content)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
