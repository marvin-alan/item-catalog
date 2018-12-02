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
          'description': 'Doctor: I have good news and bad news. Patient: Go with the good news first. Doctor: You have 24 hours to live. Patient: What!?! How about the bad news? Doctor: Um... I forgot to tell you yesterday.'},
         {'name': 'At the Pharmacy',
          'description': 'Woman: Can I get Viagra here? Pharmacist: Yes. Woman: Can I get it over the counter? Pharmacist: If you give me two of them, you can.'},
         {'name': 'Dental Plan',
          'description': 'I finally have a dental plan. I chew on the other side.'},
         {'name': 'Dirty Knees',
          'description': 'Q: What do you call a nurse with dirty knees? A: The head nurse.'}]],
    ['Food',
        [{'name': 'Beer Nuts vs Deer Nuts',
          'description': 'Q: Whats the difference between beer nuts and deer nuts? A: Beer nuts are $1.39, and deer nuts are under a buck.'}]],
    ['Kids',
        [{'name': 'A joke of genius',
          'description': 'Q: What did the DNA say to the other DNA? A: Do these genes make my butt look fat.'},
         {'name': 'Musical Chairs',
          'description': 'Q: What did one chair say to another chair? A: Here comes another a**hole.'}]],
    ['Marriage',
        [{'name': 'Modern Science',
          'description': 'Q: What food diminishes a womans sex drive by 90%? A: Her wedding cake.'}]],
    ['Work',
        [{'name': 'For the unemployed',
          'description': 'A man went to apply for a job. After filling out his applications, he waited anxiously for the outcome. The employer said, We have an opening for people like you. Oh, thats great, the man exclaimed. What is it? The employer answered, Its called the door.'}]]
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
