from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_by_skill

app = Flask(__name__)


@app.route('/')
def get_candidates():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def get_candidate_id(candidate_id):
    candidate = get_candidate(candidate_id)
    if not candidate:
        return 'Кандидат не найден!'

    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def get_candidate_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    count_candidates = len(candidates)
    return render_template('search.html', candidates=candidates, count_candidates=count_candidates)


@app.route('/skill/<skill_name>')
def get_candidates_by_skill(skill_name):
    candidates = get_by_skill(skill_name)
    count_candidates = len(candidates)
    return render_template('skill.html', candidates=candidates, count_candidates=count_candidates, skill=skill_name)


if __name__ == '__main__':
    app.run(debug=True)
