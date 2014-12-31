import pypsum
import re


def appearance():
    import Foundation
    dark_mode = Foundation.NSUserDefaults.standardUserDefaults().persistentDomainForName_(Foundation.NSGlobalDomain).objectForKey_("AppleInterfaceStyle") == "Dark"
    return "dark" if dark_mode else "light"


def build_html(appearance, content, info):
    html = """
    <style>
        body{
            padding: 10px 12px;
            font: 15px/1.4 'Helvetica Neue';
            font-weight: 300;
        }
        h1 {
            font-size: 20px;
            font-weight: 300;
        }
        small { font-size: 12px; }
        .dark{ color: rgb(224,224,224); }
    </style>
    <body class="{{appearance}}">
        <h1>Lorem Ipsum</h1>
        {{content}}<br/><br/>
        <small>{{info}}</small>
    </body>
    """

    html = html.replace('{{appearance}}', appearance)
    html = html.replace('{{content}}', content)
    return html.replace('{{info}}', info)


types = {
    'w' : 'words',
    'p' : 'paragraphs',
    'l' : 'lists',
    'b' : 'bytes'
}


def results(fields, original_query):
    hw = re.match('([0-9]*)\ ?([wplb])?', fields['~how_what'])

    count = hw.group(1) or 1
    type = types[hw.group(2) or 'p']

    lipsum = pypsum.get_lipsum(count, type, 'no')
    output = lipsum[0].replace('\n', '<br /><br />')

    return {
        'title': 'Lorem Ipsum %s %s' % (count, type),
        'run_args': [output] ,
        'html': build_html(appearance(), output, lipsum[1]),
        'webview_transparent_background': True,
    }


def run(output):
    import os
    os.system('echo "'+output+'" | pbcopy')
