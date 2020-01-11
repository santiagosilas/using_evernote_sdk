# coding:utf-8
from evernote.edam.notestore import NoteStore
from evernote.api.client import EvernoteClient
from evernote.edam.type.ttypes import Tag, SavedSearch

# get the token
token = open('token').read().strip()

client = EvernoteClient(token=token, sandbox=False)
note_store = client.get_note_store()

def load_searches():
    """ return a list of searches as ['<Name>', '<Query>'] """
    searches = list()
    searches.append(['!Inbox', 'notebook:!inbox'])

    # GTD Daily Execution - Agenda
    searches.append(['GTD:Agenda', 'notebook:B-Agenda any: reminderorder:*  remindertime:* -tag:trash'])

    # GTD Daily Execution - Daily Routine Actions
    searches.append(['GTD:Daily Routine', 'notebook:B-My-Routine tag:!1.routine.daily  -tag:trash'])

    # Automatically create saved searches based in specific tags for my evernote
    tags = note_store.listTags()
    tags_context = [tag for tag in tags if tag.name.startswith('@')]
    for tag in tags_context:
        query = 'notebook:B-Next-Actions tag:%s  -tag:trash' % tag.name
        searches.append(['GTD:where' + tag.name, query])
        tags_p = [tag_p for tag_p in tags if
                      tag_p.name.startswith('!2')
                      or tag_p.name.startswith('!3')
                      or tag_p.name.startswith('!4')]
        for tag_p in tags_p:
            searches.append(['    ' + tag_p.name, query + ' tag:%s' % tag_p.name + ' -tag:trash'])

    # Projects
    searches.append(['OnGoing Projects', 'notebook:C-Projects-OnGoing tag:$0.ongoing  tag:MPN  -tag:trash'])

    # GTD Review
    searches.append(['GTD Review', 'tag:ref.organization.gtd.review  -tag:trash'])

    # ##############
    # Another stuffs
    # ##############
    searches.append(['Cache Memory', 'tag:ref..cache.memory  -tag:trash'])  # my cache memory
    searches.append(['English Reference',
                     'notebook:H-References tag:ref.english* -tag:ref.english.meaning -ref.english.done  -tag:trash'])  # english notes
    searches.append(['Me/Us/Social/Life', 'any: tag:a-1-me tag:a-2-us tag:a-3-social* tag:a-4-fun* tag:!1.routine.periodically'])
	
    searches.append(['Goals (0-2 years)', 'tag:gtd.3*'])
    searches.append(['Vision (3-5 years)', 'tag:gtd.4*'])
    searches.append(['Purpose/Life', 'tag:gtd.5*'])
    
    tags_area = [tag for tag in tags if tag.name.startswith('a-')]
    for tag_area in tags_area:
        searches.append([tag_area.name, 'tag:%s' % tag_area.name])
	
    for index in range(len(searches)):
        searches[index][0] = '%d. %s' %(index, searches[index][0])

    return searches
