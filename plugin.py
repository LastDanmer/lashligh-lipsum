import pypsum
import re

types = {
    'w' : 'words',
    'p' : 'paragraphs',
    'l' : 'lists',
    'b' : 'bytes'
}

def results(fields, original_query):
    how_what = fields['~how_what']
    hw = re.match('([0-9]*)\ ?([wplb])?', how_what)

    count = hw.group(1) or 1
    type = types[hw.group(2) or 'p']

    lipsum = pypsum.get_lipsum(count, type, 'no')
    output = lipsum[0].replace('\n', '<br /><br />')
    return {
        'title': 'Lorem Ipsum %s %s' % (count, type),
        'run_args': [output] ,
        'html': output + '<br /><br /><i>' + lipsum[1] + '</i>',
        'webview_transparent_background': True,
    }

def run(output):
    import os
    os.system('echo "'+output+'" | pbcopy')
