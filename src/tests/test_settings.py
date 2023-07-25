import pytest
from src.settings import load_settings, update_settings

def test_load_settings():
    # Assuming the settings for a user are stored in a dictionary
    settings = load_settings('current_user')
    assert isinstance(settings, dict)

def test_update_settings():
    # Assuming the settings for a user are stored in a dictionary
    old_settings = load_settings('current_user')
    new_settings = {'volume': 50, 'theme': 'dark'}
    update_settings('current_user', new_settings)
    updated_settings = load_settings('current_user')
    assert updated_settings == new_settings
    # Revert settings back to old settings after test
    update_settings('current_user', old_settings)