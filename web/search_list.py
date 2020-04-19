# Name: search_list
# Author: Reacubeth
# Time: 2020/3/16 9:26
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from django.shortcuts import render
from toolkit.initialization import neo_con
from web.data4page import trans_search_ls2json

import json


def search_list(request):

    nothing = {}
    if request.GET:
        entity = request.GET['user_text'].strip()
        db = neo_con
        tmp = db.get_search_ls_by_name(entity)
        entity_relation = json.loads(json.dumps(tmp, ensure_ascii=False))
        if len(entity_relation) == 0:
            nothing = {'title': '<h1>Sorry, Not Found in Database</h1>'}
            return render(request, 'searchList.html', {'nothing': json.dumps(nothing, ensure_ascii=False)})
        else:
            return render(request, 'searchList.html', trans_search_ls2json(entity_relation))

    return render(request, "searchList.html", {'nothing': nothing})
