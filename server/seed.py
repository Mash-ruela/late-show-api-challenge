import os
from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User  # Assuming you want to seed this later

print("✅ seed.py started")

try:
    from server.app import create_app, db
    print("✅ App and DB imported")

    from server.models.guest import Guest
    from server.models.episode import Episode
    from server.models.appearance import Appearance
    print("✅ Models imported")

    app = create_app()
    print("✅ App created")

    with app.app_context():
        print("🔄 Dropping all tables")
        db.drop_all()

        print("✅ Creating all tables")
        db.create_all()

        print("🌱 Seeding data")
        g1 = Guest(name="Zendaya", occupation="Actress")
        g2 = Guest(name="Trevor Noah", occupation="Comedian")

        e1 = Episode(date="2024-04-04", number=101)
        e2 = Episode(date="2024-04-05", number=102)

        a1 = Appearance(rating=5, guest=g1, episode=e1)
        a2 = Appearance(rating=4, guest=g2, episode=e1)

        db.session.add_all([g1, g2, e1, e2, a1, a2])
        db.session.commit()
        print("✅ Data seeded successfully")

except Exception as e:
    print("❌ ERROR:", e)

