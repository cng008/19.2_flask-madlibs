from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhh'

debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """ Show form for adding madlibs """

    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route("/story")
def see_story():
    """ Handle adding madlibs to story """

    text = story.generate(request.args)

    return render_template("story.html", text=text)