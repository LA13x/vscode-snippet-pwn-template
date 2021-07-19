_add,_free,_edit,_show = 1,2,3,4

menu = "$1"

def add(size, content):
    sla(menu, str(_add))
    sla("", str(size))
    sa("", content)

def edit(idx, content):
    sla(menu, str(_edit))
    sla("", str(idx))
    sa("", content)

def free(idx):
    sla(menu, str(_free))
    sla("", str(idx))

def show(idx):
    sla(menu, str(_show))
    sla("", str(idx))