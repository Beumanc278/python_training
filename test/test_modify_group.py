from random import randrange

from model.group import Group


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modified_name",
                  header="modified_header",
                  footer="modified_footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = [group]
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)

def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='New Group')
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = [group]
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)

def test_modify_some_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header='New header')
    group.name = old_groups[index].name
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = [group]
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
