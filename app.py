from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>همراه دیجیتال</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;800&display=swap" rel="stylesheet">
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: 'Vazirmatn', Tahoma, sans-serif;
    min-height: 100vh;
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    color: #fff;
  }

  .card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 24px;
    padding: 40px 30px;
    max-width: 520px;
    width: 100%;
    text-align: center;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
    animation: fadeUp 0.8s ease;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .logo {
    font-size: 32px;
    font-weight: 800;
    background: linear-gradient(90deg, #00d2ff, #3a7bd5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
  }

  .tagline {
    font-size: 16px;
    color: #cfd8e3;
    margin-bottom: 30px;
    line-height: 1.8;
  }

  .services {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 30px;
  }

  .service {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 16px 10px;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s ease;
  }

  .service:hover {
    background: rgba(0, 210, 255, 0.15);
    border-color: #00d2ff;
    transform: translateY(-4px);
  }

  .soon {
    font-size: 15px;
    color: #ffd166;
    font-weight: 600;
    margin-bottom: 28px;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }

  .contacts {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .contact {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.06);
    border-radius: 14px;
    padding: 12px 18px;
    text-decoration: none;
    color: #fff;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
  }

  .contact:hover {
    background: rgba(58, 123, 213, 0.25);
    border-color: #3a7bd5;
  }

  .contact span:first-child {
    font-size: 14px;
    color: #aab7c4;
  }

  .contact span:last-child {
    font-weight: 700;
    color: #00d2ff;
    direction: ltr;
  }
</style>
</head>
<body>

  <div class="card">
    <div class="logo">همراه دیجیتال</div>
    <p class="tagline">همراه دیجیتال، برای پیشرفت ایران 🇮🇷</p>

    <div class="services">
      <div class="service">طراحی سایت 🌐</div>
      <div class="service">ربات سروش و روبیکا 🤖</div>
      <div class="service">هوش مصنوعی 🧠</div>
      <div class="service">انواع پروژه‌ها 👨‍💻</div>
    </div>

    <p class="soon">به زودی فعالیت ما آغاز می‌شود...</p>

    <div class="contacts">
      <a class="contact" href="https://rubika.ir/rubika5030" target="_blank">
        <span>آیدی روبیکا</span>
        <span>@rubika5030</span>
      </a>
      <a class="contact" href="#" target="_blank">
        <span>آیدی سروش</span>
        <span>@hamrah5030</span>
      </a>
    </div>
  </div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
