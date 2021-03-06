import path_helper_test_main
import pytest
from pytest_mock import mocker
from snail import *

class mock_Controller(object):

    def create_temp_photo(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def piv_right(self):
        pass

    def piv_left(self):
        pass

    def clear_current_image_folder(self):
        pass


# mock functions
def mock_AI_func(*arg):
    return 'forward'

def mock_user_supervisor_func():
    return "I am being called"

def mock_image_path():
    return 'an image path'

# tests
def test_AI_loop_calls_create_temp_photo(mocker):
    mocker.patch.object(mock_Controller, 'create_temp_photo')
    AI_loop(counter=0, ai=mock_AI_func, user=mock_user_supervisor_func, control=mock_Controller)
    assert mock_Controller.create_temp_photo.called

def test_AI_loop_calls_AI_function_and_applies_motion(mocker):
    mocker.patch.object(mock_Controller, 'create_temp_photo')
    mocker.patch.object(mock_Controller, 'up')
    AI_loop(counter=1,
        ai=mock_AI_func,
        user=mock_user_supervisor_func,
        img_path=mock_image_path,
        control=mock_Controller)
    assert mock_Controller.up.called

def test_AI_loop_calls_user_supervision_func_after_counter_reaches_target(mocker):
    assert (AI_loop(counter=0,
            ai=mock_AI_func,
            user=mock_user_supervisor_func,
            img_path=mock_image_path,
            control=mock_Controller)
            ) == "I am being called"
