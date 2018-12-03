from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *

engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categories = [
    ['Doctor',
        [{'name': 'Bad News',
          'description': 'Doctor: I have good news and bad news.'},
         {'name': 'At the Pharmacy',
          'description': 'Woman: Can I get Viagra here? Pharmacist: Maybe.'},
         {'name': 'Dental Plan',
          'description': 'I finally got dental plan. I chew the other side.'},
         {'name': 'Dirty Knees',
          'description': 'Q: What do you call a nurse with dirty knees?.'}]],
    ['Food',
        [{'name': 'Beer Nuts vs Deer Nuts',
          'description': 'Beer nuts are 1.39, deer nuts are under a buck.'}]],
    ['Kids',
        [{'name': 'A joke of genius',
          'description': 'Do these genes make my butt look fat.'},
         {'name': 'Musical Chairs',
          'description': 'Q: What did one chair say to another chair?'}]],
    ['Marriage',
        [{'name': 'Modern Science',
          'description': 'What food diminishes a womans sex drive by 90%?'}]],
    ['Work',
        [{'name': 'For the unemployed',
          'description': 'A man went to apply for a job.'}]]
]

current_user = User(name="Admin", email="admin@test.com")
session.add(current_user)
session.commit()

for category in categories:
    current_category = Category(name=category[0], user=current_user)
    session.add(current_category)
    session.commit()

    for item in category[1]:
        current_item = Item(name=item['name'],
                            description=item['description'],
                            category=current_category,
                            user=current_user)
        session.add(current_item)
        session.commit()

print "Demo data added!"
