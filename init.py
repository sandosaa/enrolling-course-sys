from db import session, engine
from modules import Course

subjects = [
    'Databases',
    'Computational Intelligence',
    'Data Structures',
    'Natural Language Processing',
    'Operating Systems',
    'Multi Agent Systems Design',
    'Computer Security'
]

course_map = {
    '1': 'Databases', 'DB': 'Databases',
    '2': 'Computational Intelligence', 'CI': 'Computational Intelligence',
    '3': 'Data Structures', 'DS': 'Data Structures',
    '4': 'Natural Language Processing', 'NLP': 'Natural Language Processing',
    '5': 'Operating Systems', 'OS': 'Operating Systems',
    '6': 'Multi Agent Systems Design', 'MASD': 'Multi Agent Systems Design',
    '7': 'Computer Security', 'CS': 'Computer Security'
}

for i in subjects:
    is_exist = session.query(Course).filter_by(subject=i).first()
    if not is_exist:
        session.add(Course(subject=i))
        session.commit()