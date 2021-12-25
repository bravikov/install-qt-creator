from urllib import request
from urllib.error import HTTPError
import unittest


def binary_search(first: int, last: int, find):
    while first < last - 1:
        mid = first + (last - first) // 2
        if find(mid):
            first = mid
        else:
            last = mid
    return first if find(first) else None


class TestBinarySearch(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, binary_search(4, 100, lambda x: True if x <= 6 else False))
        self.assertEqual(0, binary_search(0, 100, lambda x: True if x <= 0 else False))
        self.assertEqual(1, binary_search(0, 20, lambda x: True if x <= 1 else False))
        self.assertEqual(15, binary_search(0, 100, lambda x: True if x <= 15 else False))
        self.assertEqual(3, binary_search(0, 100, lambda x: True if x <= 3 else False))
        self.assertEqual(99, binary_search(0, 100, lambda x: True))
        self.assertEqual(None, binary_search(0, 20, lambda x: False))


def check_url(url):
    try:
        status_code = request.urlopen(url).getcode()
        return status_code == 200
    except HTTPError:
        return False


base_url = 'https://download.qt.io/official_releases/qtcreator'


def find_major_version(major_version):
    url = f'{base_url}/{major_version}.0/'
    return check_url(url)


def find_minor_version(major_version):
    def find(minor_version):
        url = f'{base_url}/{major_version}.{minor_version}/'
        return check_url(url)
    return find


def find_patch_version(major_version, minor_version):
    def find(patch_version):
        url = f'{base_url}/{major_version}.{minor_version}/{major_version}.{minor_version}.{patch_version}/'
        return check_url(url)
    return find


def main():
    major_version = binary_search(4, 20, find_major_version)
    minor_version = binary_search(0, 20, find_minor_version(major_version))
    patch_version = binary_search(0, 20, find_patch_version(major_version, minor_version))
    print(f'{major_version} {minor_version} {patch_version}')


if __name__ == '__main__':
    main()
