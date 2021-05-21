from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='test', header="testtest", footer="test1"))
    app.group.delete_first()