# test_app.py
import pytest
from main import get_count_of_cache_container_images

def test_get_count_of_cache_container_images():
    images = get_count_of_cache_container_images()
    assert len(images) == 2, "Images count for Testbed must be 2"

def test_ubuntu_container_image_exists():
    images = get_count_of_cache_container_images()
    assert images.__contains__('docker.io/library/ubuntu'), "Ubuntu Image must Exist"