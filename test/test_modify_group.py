from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = app.group.get_group_list()
    group = Group(name="modified_name",
                  header="modified_header",
                  footer="modified_footer")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = app.group.get_group_list()
    group = Group(name='New Group')
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = app.group.get_group_list()
    group = Group(header='New header')
    group.name = old_groups[0].name
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
