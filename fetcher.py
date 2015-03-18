#!/usr/bin/python

import requests
import StringIO
import xml.etree.ElementTree as ET

reference_filename = 'reference.html'

def main():
    diff = fetch_and_compare()

    if len(diff) > 0:
        return 1

    # grab pdf's from individual links

    # merge pdf's

    # send email w/ pdf attached


def fetch_and_compare(url='http://www.yalelawtech.org/cpt/', 
                      xpath='//*[@id="post-703"]/div/div[1]'):
    new_data = requests.get(url).text.encode('utf-8')
    new_tree = ET.fromstring(new_data)

    old_tree = ET.parse(reference_filename)

    print len(new_tree) + '\n\n!!!!!!!!!!!!!!!!!!!!\n\n' + len(old_tree)

    # diff old and new data
    diff = diff(new_tree, old_tree)

    # update reference.html
    update_reference(new_data)

    # return diff


# from http://stackoverflow.com/questions/6486450/python-compute-list-difference
def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]


# update old reference.html file to new contents
def update_reference(new_data):
    if len(new_data) == 0:
        return false

    output = open(reference_filename, 'w')
    output.write(new_data)
    output.close()
    return true


if __name__ == '__main__':
    main()