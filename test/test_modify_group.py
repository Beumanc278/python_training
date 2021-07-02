import random

from model.group import Group


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="modified_name",
                      header="modified_header",
                      footer="modified_footer")
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[old_groups.index(group)] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name='New Group')
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group)] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_modify_some_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Name',
                               header='Header',
                               footer='Footer'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(header='New header')
    new_group.name = group.name
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group)] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
