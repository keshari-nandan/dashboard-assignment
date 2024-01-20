from datetime import datetime
import typer

from app.core.database import SessionLocal
from app.core.security import hash_password
from app.models.user import UserModel
from app.services.fake import ensure_fake_data, add_fake_transactions
from app.models.dashboard import DashboardModel

app = typer.Typer()


@app.command()
def seed(start_date: str, end_date: str = None, per_day: int = 10):
    email = input("What is your email? ")
    with SessionLocal() as db:
        user = db.query(UserModel).filter(UserModel.email == email).first()
        if not user:
            name = input("What is your full name? ")
            password = input("What is your password? ")
            names = name.split(" ")
            if len(names) != 2:
                print("Please enter first name & last name, separated by space")
                return
            user = UserModel()
            user.first_name = names[0]
            user.last_name = names[1]
            user.email = email
            user.password = hash_password(password)
            user.is_active = True
            user.is_demo = True
            user.verified_at = datetime.now()
            db.add(user)
            db.commit()
            db.refresh(user)

        # Ensure Fake Data Exists
        ensure_fake_data(user, db)
        add_fake_transactions(db, user, start_date, end_date, per_day)
        
        # Ensure user dashboard
        dashboard = db.query(DashboardModel).filter(DashboardModel.user_id == user.id).first()
        if not dashboard:
            dashboard = DashboardModel()
            dashboard.user_id = user.id
            dashboard.name = "My Dashboard"
            db.add(dashboard)
            db.commit()
            db.refresh(dashboard)
        
        


if __name__ == "__main__":
    app()
