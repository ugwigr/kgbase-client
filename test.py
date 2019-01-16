import client


a = client.Client('ab')

# a.project_list()

print a.project_create(**{
    'name': 'client-test-name23',
    'description': 'client-test-description1',
    'is_public': 1
})