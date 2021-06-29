# -*- coding: utf-8 -*-

from model.group import Group
import pytest


testdata = [Group(name=name, header=header, footer=footer)
            for name in ['', Group.generate_random_group_field('name', 10)]
            for header in ['', Group.generate_random_group_field('header', 20)]
            for footer in ['', Group.generate_random_group_field('footer', 20)]]


@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
