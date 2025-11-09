from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        "name": "Anshika",
        "title": "Engineering Student • Innovator • Tech Explorer",
        "intro": (
            "Hi! I'm Anshika — an engineering student passionate about AI, design, and innovation. "
            "I love blending creativity with technology to craft meaningful, aesthetic, and smart projects."
        ),
        "bio": (
            "My strengths lie in problem-solving, applied AI, and building user-focused digital experiences. "
            "I enjoy transforming ideas into functional prototypes that combine creativity and logic."
        ),
        "email": "anshikasuruchi@gmail.com",
        "location": "Udupi, India",
        "linkedin": "https://www.linkedin.com/in/anshika-a-494189262",
        "github": "https://github.com/Anshika-17a",
    }

    education = [
        {
            "degree": "Bachelor of Engineering (B.E.), Artificial Intelligence Machine Learning",
            "institution": "Shri Madhwa Vadiraja Institute of Technology & Management",
            "year": "2023 — Present",
            "notes": "Focused on Artificial Intelligence, Cybersecurity, and Full Stack Development."
        },
        {
            "degree": "Pre-University (Science Stream)",
            "institution": "City Montessori School, Lucknow",
            "year": "2021 — 2023",
            "notes": "Specialized in Physics, Chemistry, Mathematics, and Computer Science."
        },
        {
            "degree": "High School (Class 10)",
            "institution": "City Montessori School, Lucknow",
            "year": "2012 — 2021",
            "notes": "Graduated with distinction and early passion for computer science and design."
        }
    ]

    projects = [
        {
            "title": "Suraksha Kavach",
            "summary": "An AI-powered cybersecurity system that detects malicious text and media to prevent scams and phishing.",
            "tech": ["FastAPI", "Transformers", "OpenCV"]
        },
        {
            "title": "Hotel Management System",
            "summary": "A full-stack DBMS app built with Flask and MySQL for efficient hotel data management and guest handling.",
            "tech": ["Flask", "MySQL", "HTML", "CSS"]
        },
        {
            "title": "FinTech Early Warning System",
            "summary": "An AI-driven FinTech system that predicts potential loan defaulters using behavioral and financial analytics.",
            "tech": ["Python", "XGBoost", "Pandas", "Flask"]
        },
        {
            "title": "JanScribe",
            "summary": "An NLP-based note-taking tool that summarizes large texts into clear, concise insights.",
            "tech": ["Python", "Transformers", "Flask"]
        }
    ]

    skills = ["Python", "HTML", "CSS", "Java", "SQL", "MongoDB", "AI/ML", "C"]

    hobbies = [
        "Designing creative projects",
        "Reading (especially self-growth & tech articles)",
        "Dancing",
        "Exploring new cafés & places",
        "Listening to music",
        "Watching tech documentaries"
    ]

    return render_template("index.html",
                           profile=profile,
                           education=education,
                           projects=projects,
                           skills=skills,
                           hobbies=hobbies)


if __name__ == '__main__':
    app.run(debug=True)
