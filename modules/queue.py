"""
.queue - list management
author: mattr555
"""

import os
import pickle
<<<<<<< HEAD
import random
<<<<<<< HEAD
import more
=======
>>>>>>> 2674acc... Add queue move, replace, random

<<<<<<< HEAD
<<<<<<< HEAD
commands = '.queue display, .queue new, .queue delete, .queue rename, .queue <name> add, .queue <name> swap, .queue <name> remove, .queue <name> pop'
=======
commands = '.queue display, .queue new, .queue delete, .queue <name> add, .queue <name> swap, .queue <name> remove, .queue <name> pop'
>>>>>>> 0a2c8bc... added ability to have duplicate queues
=======
commands = '.queue display, .queue new, .queue delete, .queue <name> add, .queue <name> swap, .queue <name> remove'
>>>>>>> 6d4cf2a... added delete command .queue

commands = '.queue display, .queue new, .queue <name> add, .queue <name> swap, .queue <name> remove'
=======
>>>>>>> f3f98a7... added .queue (new, display, add, delete, swap)

def filename(phenny):
    name = phenny.nick + '-' + phenny.config.host + '.queue.db'
    return os.path.join(os.path.expanduser('~/.phenny'), name)

def write_dict(filename, data):
    with open(filename, 'wb') as f:
        f.write(pickle.dumps(data))

def read_dict(filename):
    data = None
    with open(filename, 'rb') as f:
        data = pickle.loads(f.read())
    return data

def setup(phenny):
    f = filename(phenny)
    if os.path.exists(f):
        phenny.queue_data = read_dict(f)
    else:
        phenny.queue_data = {}

def search_queue(queue, query):
<<<<<<< HEAD
    index = None
    for i in range(len(queue)):
<<<<<<< HEAD
        if queue[i].lower().startswith(query.lower()):
=======
        if query.lower() in queue[i].lower():
>>>>>>> 98d0772... better parsing by lowercasing .queue
=======
    for i in range(len(queue)):
        if query in queue[i]:
>>>>>>> f3f98a7... added .queue (new, display, add, delete, swap)
            index = int(i)
            break
    return index

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def get_queue(queue_data, queue_name, nick):
    lower_names = {k.lower(): k for k in queue_data.keys()}
    if queue_name.lower() in lower_names:
        n = lower_names[queue_name.lower()]
        return n, queue_data[n]
    elif nick.lower() + ':' + queue_name.lower() in lower_names:
        n = lower_names[nick.lower() + ':' + queue_name.lower()]
        return n, queue_data[n]
    else:
        for i in lower_names:
            if queue_name.lower() == i.split(':')[1]:
                n = lower_names[i.lower()]
                return n, queue_data[n]
    return None, None

def disambiguate_name(queue_data, queue_name):
    matches = []
    for i in queue_data:
        if queue_name == i:
            return i
        if queue_name.lower() in i.lower():
            matches.append(i)
    return matches[0] if len(matches) == 1 else matches
=======
def search_queue_list(queue_data, queue_name, nick):
    if queue_name in queue_data:
        return queue_name, queue_data[queue_name]
    elif nick + ':' + queue_name in queue_data:
        n = nick + ':' + queue_name
        return n, queue_data[n]
    else:
        for i in queue_data:
            if queue_name == i.split(':')[1]:
                return i, queue_data[i]
    return None, None 
>>>>>>> 0a2c8bc... added ability to have duplicate queues

def print_queue(queue_name, queue):
    return '[{}]- {}'.format(
        queue_name, ', '.join(queue['queue']) if queue['queue'] else '<empty>')
=======
def print_queue(queue_name, queue):
    return '[{}] (by {}): {}'.format(
        queue_name, queue['owner'], ', '.join(queue['queue']) if queue['queue'] else '<empty>')
>>>>>>> 050e15c... better .queue formatting, dict writing bug

def queue(phenny, raw):
    """.queue- queue management."""
    if raw.group(1):
<<<<<<< HEAD
        command = raw.group(1)
        if command.lower() == 'display':
<<<<<<< HEAD
            search = raw.group(2)
<<<<<<< HEAD
            if search:
                queue_names = disambiguate_name(phenny.queue_data, search)
                if type(queue_names) is str:
                    #there was only one possible queue
                    phenny.reply(print_queue(queue_names, phenny.queue_data[queue_names]))
                elif len(queue_names) > 0:
                    #the name was ambiguous, show a list of queues
                    phenny.reply('Did you mean: ' + ', '.join(queue_names) + '?')
                else:
                    phenny.reply('No queues found.')
=======
            queue_name, queue = search_queue_list(phenny.queue_data, search, raw.nick)
            if queue_name:
=======
=======
        command = raw.group(1).lower()
        if command == 'display':
>>>>>>> 98d0772... better parsing by lowercasing .queue
            queue_name = raw.group(2)
            if queue_name in phenny.queue_data:
                queue = phenny.queue_data[queue_name]
<<<<<<< HEAD
>>>>>>> 3f1be4f... fixed lowercasing in .queue
                phenny.reply(print_queue(queue_name, queue))
>>>>>>> 0a2c8bc... added ability to have duplicate queues
=======
                phenny.reply(print_queue(queue_name, queue))
>>>>>>> 050e15c... better .queue formatting, dict writing bug
            else:
                #there was no queue name given, display all of their names
                if phenny.queue_data:
                    phenny.reply('Avaliable queues: ' + ', '.join(sorted(phenny.queue_data.keys())))
                else:
                    phenny.reply('There are no queues to display.')

        elif command.lower() == 'new':
            if raw.group(2):
                queue_name = raw.nick + ':' + raw.group(2)
                owner = raw.nick
                if queue_name not in phenny.queue_data:
                    if raw.group(3):
                        queue = raw.group(3).split(',')
                        queue = list(map(lambda x: x.strip(), queue))
                        phenny.queue_data[queue_name] = {'owner': owner, 'queue': queue}
                        write_dict(filename(phenny), phenny.queue_data)
                        phenny.reply('Queue {} with items {} created.'.format(
                            queue_name, ', '.join(queue)))
                    else:
                        phenny.queue_data[queue_name] = {'owner': owner, 'queue': []}
                        write_dict(filename(phenny), phenny.queue_data)
                        phenny.reply('Empty queue {} created.'.format(queue_name))
                else:
<<<<<<< HEAD
                    phenny.reply('You already have a queue with that name! Pick a new name or delete the old one.')
=======
                    phenny.reply('A queue with that name already exists. Pick a new name.')
>>>>>>> 09b8613... fixed duplicate name .queue
            else:
                phenny.reply('Syntax: .queue new <name> <item1>, <item2> ...')

        elif command.lower() == 'delete':
            if raw.group(2):
<<<<<<< HEAD
<<<<<<< HEAD
                queue_name, queue = get_queue(phenny.queue_data, raw.group(2), raw.nick)
                if type(queue_name) is str:
                    if raw.nick == queue['owner'] or raw.admin:
                        phenny.queue_data.pop(queue_name)
                        write_dict(filename(phenny), phenny.queue_data)
                        phenny.reply('Queue {} deleted.'.format(queue_name))
                    else:
                        phenny.reply('You aren\'t authorized to do that!')
                else:
                    phenny.reply('That queue wasn\'t found!')
            else:
                phenny.reply('Syntax: .queue delete <name>')

        elif command.lower() == 'rename':
            if raw.group(3):
                queue_name, queue = search_queue_list(phenny.queue_data, raw.group(2), raw.nick)
                if raw.nick == queue['owner'] or raw.admin:
                    phenny.queue_data[queue['owner'] + ':' + raw.group(3)] = phenny.queue_data.pop(queue_name)
=======
                queue_name, queue = search_queue_list(phenny.queue_data, raw.group(2), raw.nick)
                if raw.nick == queue['owner'] or raw.admin:
                    phenny.queue_data.pop(queue_name)
>>>>>>> 0a2c8bc... added ability to have duplicate queues
                    write_dict(filename(phenny), phenny.queue_data)
                    phenny.reply(print_queue(raw.group(3), queue))
=======
                queue_name = raw.group(2)
                if raw.nick == phenny.queue_data[queue_name]['owner'] or raw.admin:
                    phenny.queue_data.pop(queue_name)
                    write_dict(filename(phenny), phenny.queue_data)
                    phenny.reply('Queue {} deleted.'.format(queue_name))
>>>>>>> 6d4cf2a... added delete command .queue
                else:
                    phenny.reply('You aren\'t authorized to do that!')
            else:
                phenny.reply('Syntax: .queue delete <name>')

<<<<<<< HEAD
        elif search_queue_list(phenny.queue_data, raw.group(1), raw.nick)[0]:
=======
        elif command in phenny.queue_data:
>>>>>>> 6d4cf2a... added delete command .queue
            #queue-specific commands
<<<<<<< HEAD
            queue_name, queue = get_queue(phenny.queue_data, raw.group(1), raw.nick)
=======
            queue_name, queue = search_queue_list(phenny.queue_data, raw.group(1), raw.nick)
>>>>>>> 0a2c8bc... added ability to have duplicate queues
            if raw.group(2):
                command = raw.group(2).lower()
<<<<<<< HEAD
                if queue['owner'] == raw.nick or raw.admin:
=======
                if queue['owner'] == raw.nick:
>>>>>>> 98d0772... better parsing by lowercasing .queue
=======
def queue(phenny, raw):
    """.queue- queue management."""
    if raw.group(1):
        command = raw.group(1)
        if command == 'display':
            queue_name = raw.group(2)
            if queue_name in phenny.queue_data:
                queue = phenny.queue_data[queue_name]
                phenny.reply('{} queue by {}: {}'.format(
                    queue_name, queue['owner'], ', '.join(queue['queue']) if queue['queue'] else '<empty>'))
            else:
                phenny.reply('That queue wasn\'t found.')

        elif command == 'new':
            if raw.group(2):
                queue_name = raw.group(2)
                owner = raw.nick
                if raw.group(3):
                    queue = raw.group(3).split(',')
                    queue = list(map(lambda x: x.strip(), queue))
                    phenny.queue_data[queue_name] = {'owner': owner, 'queue': queue}
                    write_dict(filename(phenny), phenny.queue_data)
                    phenny.reply('Queue {} with items {} created.'.format(
                        queue_name, ', '.join(queue)))
                else:
                    phenny.queue_data[queue_name] = {'owner': owner, 'queue': []}
                    write_dict(filename(phenny), phenny.queue_data)
                    phenny.reply('Empty queue {} created.'.format(queue_name))
            else:
                phenny.reply('Syntax: .queue new <name> <item1>, <item2> ...')

        elif command in phenny.queue_data:
            #queue-specific commands
            queue_name = raw.group(1)
            queue = phenny.queue_data[queue_name]
            if raw.group(2):
                command = raw.group(2)
                if queue['owner'] == raw.nick:
>>>>>>> f3f98a7... added .queue (new, display, add, delete, swap)
                    if command == 'add':
                        if raw.group(3):
                            new_queue = raw.group(3).split(',')
                            new_queue = list(map(lambda x: x.strip(), new_queue))
                            queue['queue'] += new_queue
                            write_dict(filename(phenny), phenny.queue_data)
<<<<<<< HEAD
                            phenny.reply(print_queue(queue_name, queue))
=======
                            phenny.reply('{} queue by {}: {}'.format(
                                queue_name, queue['owner'], ', '.join(queue['queue'])))
>>>>>>> f3f98a7... added .queue (new, display, add, delete, swap)
                        else:
                            phenny.reply('Syntax: .queue <name> add <item1>, <item2> ...')
                    elif command == 'swap':
                        if raw.group(3):
                            indices = raw.group(3).split(',')
                            try:
                                id1, id2 = tuple(map(lambda x: int(x.strip()), indices))[:2]
                            except ValueError:
                                q1, q2 = tuple(map(lambda x: x.strip(), indices))[:2]
                                id1 = search_queue(queue['queue'], q1)
                                if id1 is None:
                                    phenny.reply('{} not found in {}'.format(indices[0].strip(), queue_name))
                                    return
                                id2 = search_queue(queue['queue'], q2)
                                if id2 is None:
                                    phenny.reply('{} not found in {}'.format(indices[1].strip(), queue_name))
                                    return
                            queue['queue'][id1], queue['queue'][id2] = queue['queue'][id2], queue['queue'][id1]
                            write_dict(filename(phenny), phenny.queue_data)
<<<<<<< HEAD
                            phenny.reply(print_queue(queue_name, queue))
                        else:
                            phenny.reply('Syntax: .queue <name> swap <index/item1>, <index/item2>')
<<<<<<< HEAD
<<<<<<< HEAD
                    elif command == 'move' or command == 'mv':
=======
                    elif command == 'move':
>>>>>>> 2674acc... Add queue move, replace, random
                        if raw.group(3) and ',' in raw.group(3):
                            indices = raw.group(3).split(',')
                            try:
                                id1, id2 = tuple(map(lambda x: int(x.strip()), indices))[:2]
                            except ValueError:
                                q1, q2 = tuple(map(lambda x: x.strip(), indices))[:2]
                                id1 = search_queue(queue['queue'], q1)
                                if id1 is None:
                                    phenny.reply('{} not found in {}'.format(indices[0].strip(), queue_name))
                                    return
                                id2 = search_queue(queue['queue'], q2)
                                if id2 is None:
                                    phenny.reply('{} not found in {}'.format(indices[1].strip(), queue_name))
                                    return
<<<<<<< HEAD
                            #queue['queue'][id2 + (-1 if id1 < id2 else 0)] = queue['queue'].pop(id1)
                            queue['queue'].insert(id2, queue['queue'].pop(id1))
=======
                            queue['queue'][id2 + (-1 if id1 < id2 else 0)] = queue['queue'].pop(id1)
>>>>>>> 2674acc... Add queue move, replace, random
                            write_dict(filename(phenny), phenny.queue_data)
                            phenny.reply(print_queue(queue_name, queue))
                        else:
                            phenny.reply('Syntax: .queue <name> move <source_index/item>, <target_index/item>')
                    elif command == 'replace':
                        if raw.group(3) and ',' in raw.group(3):
                            old, new = raw.group(3).split(',')
                            old = old.strip()
                            try:
                                old_id = int(old)
                            except ValueError:
                                old_id = search_queue(queue['queue'], old)
                                if old_id is None:
                                    phenny.reply('{} not found in {}'.format(old, queue_name))
                                    return
                            queue['queue'][old_id] = new.strip()
                            write_dict(filename(phenny), phenny.queue_data)
                            phenny.reply(print_queue(queue_name, queue))
                        else:
                            phenny.reply('Syntax: .queue <name> replace <index/item>, <new_item>')
<<<<<<< HEAD
                    elif command == 'remove' or command == 'delete':
=======
=======
>>>>>>> 98d0772... better parsing by lowercasing .queue
                    elif command == 'remove':
=======
                            phenny.reply('{} queue by {}: {}'.format(
                                queue_name, queue['owner'], ', '.join(queue['queue'])))
                        else:
                            phenny.reply('Syntax: .queue <name> swap <index/item1>, <index/item2>')
                    elif command in ('delete', 'remove'):
>>>>>>> f3f98a7... added .queue (new, display, add, delete, swap)
                        if raw.group(3):
                            item = raw.group(3)
                            if item in queue['queue']:
                                queue['queue'].remove(item)
<<<<<<< HEAD
                                write_dict(filename(phenny), phenny.queue_data)
                                phenny.reply(print_queue(queue_name, queue))
                            elif search_queue(queue['queue'], item):
                                queue['queue'].pop(search_queue(queue['queue'], item))
                                write_dict(filename(phenny), phenny.queue_data)
                                phenny.reply(print_queue(queue_name, queue))
=======
                                phenny.reply('{} queue by {}: {}'.format(
                                    queue_name, queue['owner'], ', '.join(queue['queue'])))
                            elif search_queue(queue['queue'], item):
                                queue['queue'].pop(search_queue(queue['queue'], item))
                                phenny.reply('{} queue by {}: {}'.format(
                                    queue_name, queue['owner'], ', '.join(queue['queue'])))
>>>>>>> f3f98a7... added .queue (new, display, add, delete, swap)
                            else:
                                phenny.reply('{} not found in {}'.format(item, queue_name))
                        else:
                            phenny.reply('Syntax: .queue <name> remove <item>')
<<<<<<< HEAD
                    elif command == 'pop':
<<<<<<< HEAD
                        try:
                            queue['queue'].pop(0)
                            write_dict(filename(phenny), phenny.queue_data)
                            phenny.reply(print_queue(queue_name, queue))
                        except IndexError:
                            phenny.reply('That queue is already empty.')
<<<<<<< HEAD
                    elif command == 'random':
                        phenny.reply('%s is the lucky one.' % repr(random.choice(queue['queue'])))
                    elif command == 'reassign':
                        if raw.group(3):
                            new_owner = raw.group(3)
                            new_queue_name = new_owner + queue_name[queue_name.index(':'):]
                            phenny.queue_data.pop(queue_name)
                            phenny.queue_data[new_queue_name] = {'owner': new_owner, 'queue': queue['queue']}
                            write_dict(filename(phenny), phenny.queue_data)
                            phenny.reply(print_queue(new_queue_name, queue))
                        else:
                            phenny.reply('Syntax: .queue <name> reassign <nick>')
                    elif command.lower() in ['rename', 'ren']:
                        if raw.group(3):
                            new_queue_name = queue['owner'] + ':' + raw.group(3)
                            phenny.queue_data[new_queue_name] = phenny.queue_data.pop(queue_name)
                            write_dict(filename(phenny), phenny.queue_data)
                            phenny.reply(print_queue(new_queue_name, queue))
                        else:
                            phenny.reply('Syntax: .queue <name> rename <new_name>')
                elif command == 'random':
                    phenny.reply('%s is the lucky one.' % repr(random.choice(queue['queue'])))
=======
>>>>>>> 0a2c8bc... added ability to have duplicate queues
=======
                        queue['queue'].pop(0)
                        write_dict(filename(phenny), phenny.queue_data)
                        phenny.reply(print_queue(queue_name, queue))
>>>>>>> e2db73b... added pop command .queue
                else:
                    phenny.reply('You aren\'t the owner of this queue!')
            else:
                phenny.reply(print_queue(queue_name, queue))
        else:
            if raw.group(3):
                phenny.reply('That\'s not a command. Commands: ' + commands)
            else:
                phenny.reply('That queue wasn\'t found!')
    else:
        phenny.reply('Commands: ' + commands)

queue.rule = r'\.queue(?:\s([a-zA-Z0-9:_]+))?(?:\s(\w+))?(?:\s(.*))?'
=======
                else:
                    phenny.reply('You aren\'t the owner of this queue!')
            else:
                phenny.reply('{} queue by {}: {}'.format(
                    queue_name, queue['owner'], ', '.join(queue['queue']) if queue['queue'] else '<empty>'))
        else:
            if raw.group(3):
                phenny.reply('That\'s not a command. Commands: .queue display, .queue new, .queue <name> add, .queue <name> swap')
            else:
                phenny.reply('That queue wasn\'t found!')
    else:
        phenny.reply('Commands: .queue display, .queue new, .queue <name> add, .queue <name> swap')

queue.rule = r'\.queue(?:\s(\w+))?(?:\s(\w+))?(?:\s(.*))?'
>>>>>>> f3f98a7... added .queue (new, display, add, delete, swap)
