"""users table

Revision ID: 002a2be91662
Revises: 2f35caa285c4
Create Date: 2022-01-02 19:24:28.594554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002a2be91662'
down_revision = '2f35caa285c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prenotation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_cognome', sa.String(length=120), nullable=True),
    sa.Column('tel', sa.String(length=120), nullable=True),
    sa.Column('check_in', sa.Date(), nullable=True),
    sa.Column('ospiti', sa.String(length=120), nullable=True),
    sa.Column('struttura', sa.String(length=120), nullable=True),
    sa.Column('user_email', sa.String(length=120), nullable=True),
    sa.Column('check_out', sa.Date(), nullable=True),
    sa.Column('stanza', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['user_email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_prenotation_check_in'), 'prenotation', ['check_in'], unique=False)
    op.create_index(op.f('ix_prenotation_check_out'), 'prenotation', ['check_out'], unique=False)
    op.create_index(op.f('ix_prenotation_nome_cognome'), 'prenotation', ['nome_cognome'], unique=False)
    op.create_index(op.f('ix_prenotation_ospiti'), 'prenotation', ['ospiti'], unique=False)
    op.create_index(op.f('ix_prenotation_stanza'), 'prenotation', ['stanza'], unique=False)
    op.create_index(op.f('ix_prenotation_struttura'), 'prenotation', ['struttura'], unique=False)
    op.create_index(op.f('ix_prenotation_tel'), 'prenotation', ['tel'], unique=False)
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.VARCHAR(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DATETIME(), nullable=True))
    op.drop_index(op.f('ix_prenotation_tel'), table_name='prenotation')
    op.drop_index(op.f('ix_prenotation_struttura'), table_name='prenotation')
    op.drop_index(op.f('ix_prenotation_stanza'), table_name='prenotation')
    op.drop_index(op.f('ix_prenotation_ospiti'), table_name='prenotation')
    op.drop_index(op.f('ix_prenotation_nome_cognome'), table_name='prenotation')
    op.drop_index(op.f('ix_prenotation_check_out'), table_name='prenotation')
    op.drop_index(op.f('ix_prenotation_check_in'), table_name='prenotation')
    op.drop_table('prenotation')
    # ### end Alembic commands ###
