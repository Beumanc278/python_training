from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    app.group.modify_first_group(Group(name="modified_name",
                                       header="modified_header",
                                       footer="modified_footer"))

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    app.group.modify_first_group(Group(name='New Group'))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    app.group.modify_first_group(Group(header='New header'))
