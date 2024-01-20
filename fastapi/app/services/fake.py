import time
from datetime import datetime, timedelta
import random

from rich.console import Console
from rich.progress import track
from sqlalchemy.orm import joinedload

from app.models.bank import BankModel
from app.models.card import CardModel
from app.models.category import CategoryModel
from app.models.expense import TagModel, ExpenseModel
from app.models.user import UserModel

payment_modes = {
    "UPI": "UPI",
    "CASH": "Cash",
    "CARD": "Card",
    "NET_BANKING": "Net Banking",
    "IMPS": "IMPS",
    "NEFT": "NEFT",
    "RTGS": "RTGS",
    "CHEQUE": "Cheque",
    "ACH": "ACH",
    "DD": "Demand Draft",
    "OTHERS": "Others",
}

categories = {
    'Food': ['Zomato', 'Swiggy', "DineIn", "UberEat", "EatSure"],
    'Groceries': ['Amazon', 'Flipkart', 'Snapdeal', 'JioMart', 'BigBasket', "Store"],
    'Cosmetics': ["Lipstick", "Face Cream", "Night Cream", "Rose Water"],
    'Electronics': ["Mobile", "Laptop", "Tablet", "Camera", "Television"],
    'Medical': ["OPD", "Manipal", "Lab Test", "Medicine", "Parking"],
    'Gift': ["Gift Card", "Gift Voucher", "Parking"],
    'Education': ["Hostel Fee", "Semester Fee", "Pocket Money"],
    'Bills': ["Electricity", "Water", "Gas", "Internet", "Credit Card Payment"],
    'Utilities': ["Garbage", "Parking"],
    'Travel': ["Bus", "Train", "Taxi", "Uber", "Ola", "Trip"],
    'Credit Card Payment': ["HDFC Credit Card", "Axis Credit Card", "SBI Credit Card"],
    'EMI': ["HDFC Personal Loan", "SBI Debit Card Loan", "Axis Credit Card Loan"],
    'Investment': ["Mutual Fund", "Stock", "Parking"],
    'Garments': ["Shirt", "Pants", "Shoes", "Parking"],
    'Miscellaneous': ["Parking", "Hair Cut"],
    'Subscription': ["Netflix", "Spotify", "Parking"],
    'Entertainment': ["Movie Ticket", "Amusement Park", "Parking"],
    'Shopping': ["Cloth", "Parking"],
}

banks = ['HDFC Bank', 'ICICI Bank', 'Punjab National Bank', 'State Bank of India', 'Union Bank of India', 'Axis Bank']

cards = {
    'HDFC INFINIA': "HDFC BANK",
    'SBI Elite': 'State Bank of India',
    'Axis Magnum': 'Axis Bank',
    'ICICI Amazon Pay': 'ICICI Bank'
}


def _ensure_categories_and_tags_exists(user, db, console):
    user_categories = [] if not user.categories else [obj.id for obj in user.categories]
    console.log("Ensuring the user categories...")
    time.sleep(1)
    for category, tags in categories.items():
        category_obj = db.query(CategoryModel).filter(CategoryModel.name == category).first()
        if not category_obj:
            category_obj = CategoryModel()
            category_obj.name = category
            category_obj.is_active = True
            category_obj.updated_at = datetime.now()
            db.add(category_obj)
            db.commit()
            db.refresh(category_obj)
        if category_obj.id not in user_categories:
            user.categories.append(category_obj)
            db.commit()
            db.refresh(user)
    console.log("Ensuring the user categories...Done")
    console.log("Ensuring the user tags...")
    time.sleep(1)
    for category, tags in categories.items():
        for tag in tags:
            sub_category_obj = db.query(TagModel).filter(TagModel.name == tag).first()
            if not sub_category_obj:
                sub_category_obj = TagModel()
                sub_category_obj.name = tag
                sub_category_obj.is_active = True
                sub_category_obj.updated_at = datetime.now()
                db.add(sub_category_obj)
                db.commit()
    console.log("Ensuring the user tags...Done")


def _ensure_banks_exists(user, db, console):
    console.log("Ensuring the user banks...")
    time.sleep(1)
    user_banks = [] if not user.banks else [obj.id for obj in user.banks]
    for bank in banks:
        bank_obj = db.query(BankModel).filter(BankModel.name == bank).first()
        if not bank_obj:
            bank_obj = BankModel()
            bank_obj.name = bank
            bank_obj.is_active = True
            bank_obj.updated_at = datetime.now()
            db.add(bank_obj)
            db.commit()
            db.refresh(bank_obj)
        if bank_obj.id not in user_banks:
            user.banks.append(bank_obj)
            db.commit()
    console.log("Ensuring the user banks...Done")


def _ensure_cards_exists(user, db, console):
    console.log("Ensuring the user cards...")
    user_cards = db.query(CardModel).filter(CardModel.user_id == user.id).all()
    user_card_names = [obj.name for obj in user_cards]
    user_banks = {}
    bnk_id = None
    for bank in user.banks:
        bnk_id = bank.id
        user_banks[bank.name] = bank.id
    time.sleep(1)
    for card, bnk in cards.items():
        if card not in user_card_names:
            card_obj = CardModel()
            card_obj.bank_id = user_banks.get(bnk, bnk_id)
            card_obj.name = card
            card_obj.user_id = user.id
            card_obj.is_active = True
            card_obj.type = 'Credit Card'
            card_obj.updated_at = datetime.now()
            db.add(card_obj)
            db.commit()
    console.log("Ensuring the user banks...Done")


def ensure_fake_data(user, db):
    console = Console()
    with console.status("[bold green] Ensuring the fake meta data, please wait...") as status:
        newUser = db.query(UserModel).options(joinedload(UserModel.categories), joinedload(UserModel.banks)).filter(
            UserModel.id == user.id
        ).first()

        _ensure_categories_and_tags_exists(newUser, db, console)
        _ensure_banks_exists(newUser, db, console)
        _ensure_cards_exists(newUser, db, console)


def add_fake_transactions(db, user: UserModel, start_date, end_date: str = None, per_day: int = 10):
    console = Console()
    startObj = datetime.strptime(start_date, "%Y%m%d")
    endObj = datetime.strptime(end_date, "%Y%m%d") if end_date else datetime.today()
    delta = endObj - startObj
    category_objs = db.query(CategoryModel).join(CategoryModel.users).filter(UserModel.id == user.id).filter(
        CategoryModel.name.in_(categories.keys())
    ).all()
    banks_obj = db.query(BankModel).join(BankModel.users).filter(UserModel.id == user.id).filter(
        BankModel.name.in_(banks)
    ).all()
    cards_obj = db.query(CardModel).filter(CardModel.user_id == user.id).filter(
        CardModel.name.in_(cards.keys())
    ).all()
    for i in track(range(delta.days + 1), "Adding records..."):
        current_day = startObj + timedelta(days=i)
        for j in range(per_day):
            category_obj = random.choice(category_objs)
            tags = categories.get(category_obj.name)
            check_count = 0
            while not tags:
                console.log(
                    f'{check_count + 1} Category [{category_obj.name}] does not have any tags, checking another category...')
                category_obj = random.choice(category_objs)
                tags = categories.get(category_obj.name)
                check_count += 1
                if check_count > 50:
                    console.log(f'No relevant category found after {check_count + 1} checks, Existing...')
                    break

            payment_name = random.choice(list(payment_modes.keys()))
            bank = random.choice(banks_obj)
            card = random.choice(cards_obj)
            expense = ExpenseModel()
            expense.user_id = user.id
            expense.category_id = category_obj.id
            expense.amount = random.randint(20, 50000)
            expense.date = current_day.strftime("%Y-%m-%d")
            expense.payment_mode = payment_name
            if payment_name == "CARD":
                expense.card_id = card.id
            if payment_name not in ["CARD", "CASH", "OTHER"]:
                expense.bank_id = bank.id
            expense.updated_at = datetime.now()
            db.add(expense)
            db.commit()
            db.refresh(expense)
            # Fetch all the tags
            cat_tags = db.query(TagModel).filter(TagModel.name.in_(tags)).all()
            if len(cat_tags) > 0:
                tag_count = random.randint(1, 2)
                while tag_count > 0:
                    tag = random.choice(cat_tags)
                    expense.tags.append(tag)
                    tag_count -= 1
                db.commit()

