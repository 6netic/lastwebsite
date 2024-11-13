from django.utils.html import escape


def make_newlist(old_list, question_id=None):
    """ Converts to list minus the first element and removes question_id from the list if exists """

    old_list = old_list.replace("[", "").replace("]", "").replace(" ", "")
    new_list = list(old_list.split(","))
    new_list = [int(i) for i in new_list]
    if question_id:
        new_list.remove(question_id)
    return new_list

















