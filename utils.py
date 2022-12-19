import json


def load_candidates_from_json(path):
    """
    Загружает данные из json файла
    :param path: имя файла
    :return: list
    """
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_candidate(candidate_id):
    """
    Возвращает данные кандидата по идентификатору.
    Если заданного идентификатора нет в списке - ничего не возвращается.
    :param candidate_id: int(идентификатор)
    :return: dict(данные кандидата)
    """
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return


def get_candidates_by_name(candidate_name):
    """
    Возвращает список кандидатов с одинаковыми именами
    :param candidate_name: имя кандидата
    :return: list(список кандидатов)
    """
    candidates = load_candidates_from_json('candidates.json')
    candidates_names = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidates_names.append(candidate)
    return candidates_names


def get_by_skill(skill_name):
    """
    Возвращает список кандидатов, обладающих заданным навыком(skill_name)
    :param skill_name: навык кандидата
    :return: list(список кандидатов)
    """
    candidates = load_candidates_from_json('candidates.json')
    candidates_skills = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates_skills.append(candidate)
    return candidates_skills


# print(load_candidates_from_json('candidates.json'))
# print(get_candidate(4))
# print(get_candidates_by_name('she'))
# print(get_candidates_by_skill('пользоваться календарем'))
