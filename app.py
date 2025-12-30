from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = {
    "motivational": [
        "Dream big and dare to fail.",
        "Believe you can and you're halfway there.",
        "Your future depends on what you do today.",
        "Small progress is still progress.",
        "Push yourself, because growth begins outside comfort.",
        "Wake up with determination, go to bed with satisfaction.",
        "Hard times build strong minds.",
        "Don’t stop until you’re proud.",
        "Motivation gets you started, discipline keeps you going.",
        "Success starts with self-belief."
    ],

    "life": [
        "Life is 10% what happens to us and 90% how we react to it.",
        "In the end, we only regret the chances we didn't take.",
        "Life is short, and it's up to you to make it sweet.",
        "The purpose of life is a life of purpose.",
        "Life is about making an impact, not making an income."
    ],

    "success": [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Success usually comes to those who are too busy to be looking for it.",
        "Don't be afraid to give up the good to go for the great.",
        "I find that the harder I work, the more luck I seem to have.",
        "Success is walking from failure to failure with no loss of enthusiasm."
        ],

    "self_confidence": [
        "Confidence grows with action.",
        "To follow self-confidence, you must trust your abilities, stop seeking constant approval from others, learn from mistakes without self-criticism, and respect yourself through your actions."
    ],

    "positive_thinking": [
        "Positive thoughts create positive outcomes.",
        "Train your mind to see solutions, not problems.",
        "Optimism strengthens inner peace.",
        "A positive mind attracts better opportunities.",
        "Thoughts shape your reality."
    ],

    "mental_strength": [
        "Mental strength is built through resilience.",
        "To follow mental strength, you need to stay calm under pressure, accept challenges as part of growth, control emotional reactions, and continue moving forward even when things feel difficult."
    ],

    "discipline": [
        "Discipline is freedom.",
        "To follow discipline, you must create healthy routines, stay consistent even on low-energy days, control distractions, and choose long-term benefits over short-term comfort."
    ],

    "hard_work": [
        "There are no shortcuts to any place worth going.",
        "To follow hard work, you need to set clear goals, maintain a strong work ethic, embrace challenges"
    ],

    "dreams": [
        "Dreams don't work unless you do.",
        "To follow your dreams, you must believe in them, take consistent action, overcome fear of failure, and stay patient through setbacks."
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():
    quote = None

    if request.method == "POST":
        topic = request.form.get("topic")

        if topic in quotes:
            quote = random.choice(quotes[topic])

    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
