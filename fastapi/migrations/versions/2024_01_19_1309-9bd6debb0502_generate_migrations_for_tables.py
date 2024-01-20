"""generate migrations for tables

Revision ID: 9bd6debb0502
Revises: 
Create Date: 2024-01-19 13:09:30.546085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bd6debb0502'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('logo_link', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_banks_country'), 'banks', ['country'], unique=False)
    op.create_index(op.f('ix_banks_id'), 'banks', ['id'], unique=False)
    op.create_index(op.f('ix_banks_name'), 'banks', ['name'], unique=False)
    op.create_index(op.f('ix_banks_state'), 'banks', ['state'], unique=False)
    op.create_index(op.f('ix_banks_type'), 'banks', ['type'], unique=False)
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.create_index(op.f('ix_categories_name'), 'categories', ['name'], unique=False)
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tags_id'), 'tags', ['id'], unique=False)
    op.create_index(op.f('ix_tags_name'), 'tags', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_demo', sa.Boolean(), nullable=True),
    sa.Column('verified_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.Column('card_number', sa.String(length=20), nullable=True),
    sa.Column('exp_month', sa.Integer(), nullable=True),
    sa.Column('exp_year', sa.Integer(), nullable=True),
    sa.Column('cvv', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['bank_id'], ['banks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cards_id'), 'cards', ['id'], unique=False)
    op.create_index(op.f('ix_cards_name'), 'cards', ['name'], unique=False)
    op.create_index(op.f('ix_cards_type'), 'cards', ['type'], unique=False)
    op.create_index(op.f('ix_cards_user_id'), 'cards', ['user_id'], unique=False)
    op.create_table('user_banks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['bank_id'], ['banks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_banks_id'), 'user_banks', ['id'], unique=False)
    op.create_table('user_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_categories_id'), 'user_categories', ['id'], unique=False)
    op.create_table('expenses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(precision=10, asdecimal=True), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('payment_mode', sa.String(length=50), nullable=True),
    sa.Column('card_id', sa.Integer(), nullable=True),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.Column('receipt_image', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['bank_id'], ['banks.id'], ),
    sa.ForeignKeyConstraint(['card_id'], ['cards.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expenses_amount'), 'expenses', ['amount'], unique=False)
    op.create_index(op.f('ix_expenses_date'), 'expenses', ['date'], unique=False)
    op.create_index(op.f('ix_expenses_id'), 'expenses', ['id'], unique=False)
    op.create_index(op.f('ix_expenses_payment_mode'), 'expenses', ['payment_mode'], unique=False)
    op.create_table('expense_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expense_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['expense_id'], ['expenses.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expense_tags_id'), 'expense_tags', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_expense_tags_id'), table_name='expense_tags')
    op.drop_table('expense_tags')
    op.drop_index(op.f('ix_expenses_payment_mode'), table_name='expenses')
    op.drop_index(op.f('ix_expenses_id'), table_name='expenses')
    op.drop_index(op.f('ix_expenses_date'), table_name='expenses')
    op.drop_index(op.f('ix_expenses_amount'), table_name='expenses')
    op.drop_table('expenses')
    op.drop_index(op.f('ix_user_categories_id'), table_name='user_categories')
    op.drop_table('user_categories')
    op.drop_index(op.f('ix_user_banks_id'), table_name='user_banks')
    op.drop_table('user_banks')
    op.drop_index(op.f('ix_cards_user_id'), table_name='cards')
    op.drop_index(op.f('ix_cards_type'), table_name='cards')
    op.drop_index(op.f('ix_cards_name'), table_name='cards')
    op.drop_index(op.f('ix_cards_id'), table_name='cards')
    op.drop_table('cards')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tags_name'), table_name='tags')
    op.drop_index(op.f('ix_tags_id'), table_name='tags')
    op.drop_table('tags')
    op.drop_index(op.f('ix_categories_name'), table_name='categories')
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_table('categories')
    op.drop_index(op.f('ix_banks_type'), table_name='banks')
    op.drop_index(op.f('ix_banks_state'), table_name='banks')
    op.drop_index(op.f('ix_banks_name'), table_name='banks')
    op.drop_index(op.f('ix_banks_id'), table_name='banks')
    op.drop_index(op.f('ix_banks_country'), table_name='banks')
    op.drop_table('banks')
    # ### end Alembic commands ###