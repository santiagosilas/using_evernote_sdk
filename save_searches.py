# coding:utf-8

# Description:  A Script to save my saved searches on evernote
#
#Copyright (c) 2016 Silas Santiago
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from evernote.edam.notestore import NoteStore
from evernote.api.client import EvernoteClient
from evernote.edam.type.ttypes import Tag, SavedSearch

from my_evernote_structure import load_searches

# get the token
token = open('token').read().strip()

client = EvernoteClient(token=token, sandbox=False)
note_store = client.get_note_store()


def create_searches(searches_list):

    # remove all previous searches
    for search in note_store.listSearches(token):
        note_store.expungeSearch(token, search.guid)

    # create searches on evernote
    for search in searches_list:
        saved_search = SavedSearch(name=search[0], query=search[1])
        note_store.createSearch(token, saved_search)
        print 'search created with success!'
        print '\tsearch', search[0]
        print '\tquery', search[1]
        print

if __name__ == '__main__':
    searches = load_searches()
    create_searches(searches)
    print 'done.'