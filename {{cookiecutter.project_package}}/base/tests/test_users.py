"""Tests for users model."""


from base.models import User


def test_user_tablename():
    """Tablename test && Example pytest test."""

    assert User._meta.db_table == "users"
