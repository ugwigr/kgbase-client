from github import Github
from client import Client
import time

IS_PROD = False

'''
     name      |     api_key
---------------+------------------
 Api User      | 20g6qla0yb15qzjz
 Vojtech Rinik | hPipFgouHl
 Api User      | oyzkv4vy3cci5cbw
 Gregory Ugwi  | ttFRvyGBU5
 Api User      | ttsejo1uh45dvf0n
 Sangwon Seo   | w2gJRyzNwB
 Lukas         | ZmKXnldT8R
'''

class GithubLoader(object):
    def __init__(self):
        self.github = Github("e65a450c670366efa4811ff55c7d96bf89bcf19e")
        self.repo = self.github.get_repo("thinknum/thinknum_base")

        if IS_PROD:
            self.client = Client("20g6qla0yb15qzjz")
            self.issues_table = "frontend-issues-LXPEI2mxjV6cI2nGGcn"
        else:
            self.client = Client("w2gJRyzNwB", base="http://127.0.0.1:8000/api")
            self.project = "test-github-frontend-issue5-LX_Mdum73eyjJGBYvgA"
            self.issues_table = "issues-LX_MeCWsfM7iJSob3gn"
            self.labels_table = "labels-LX_MdvCyqw1HE5n0CGv"

    # Github methods
    # ---------------------------------------------------------------

    def find_issues(self, user):
        label_high_priority = self.repo.get_label("Priority: High")
        issues = self.repo.get_issues(state="open", assignee=user, labels=[label_high_priority])
        return [issue for issue in issues]

    def find_frontend_issues(self):
        all_issues = {}

        for user in ["vojto", "lprokein"]:
            issues = self.find_issues(user)
            for issue in issues:
                all_issues[issue.number] = issue

        return all_issues.values()

    # KGbase methods
    # ---------------------------------------------------------------

    # Changesets

    def create_changeset(self):
        self.changeset_id = self.client.changeset_create(project_id=self.project, summary="Loading frontend issues from GitHub")['id']
        print("Created changeset with ID: %s" % (self.changeset_id,))

    def submit_changeset(self):
        self.client.changeset_submit(self.changeset_id)
    
    def publish_changeset(self):
        self.client.changeset_publish(self.changeset_id)

    # Labels

    def find_or_create_label(self, name):
        label = self.find_label_name(name)
        if not label:
            label = self.create_label(name)
        return label

    def find_label_name(self, name):
        labels = self.client.data_list(
            changeset_id=self.changeset_id,
            table_id=self.labels_table,
            filters={'Label': name}
        )
        return next(iter(labels), None)

    def create_label(self, name):
        label = self.client.data_create(self.changeset_id, self.labels_table, {
            'Label': name,
        })
        return label

    # Issues

    def find_issue_with_number(self, number):
        issues = self.client.data_list(
            self.changeset_id,
            self.issues_table,
            filters={'Number': number}
        )
        return next(iter(issues), None)

    def create_issue(self, data):
        return self.client.data_create(self.changeset_id, self.issues_table, data)

    def update_issue(self, issue_id, data):
        self.client.data_update(
            self.changeset_id,
            self.issues_table,
            issue_id,
            data
        )


    # Main load method
    # ---------------------------------------------------------------

    def load(self):
        # Find all Github issues
        issues = self.find_frontend_issues()

        # Start a new changeset
        self.create_changeset()

        # Store every issue
        for issue in issues:
            label_id = None
            for issue_label in issue.labels:
                label = self.find_or_create_label(issue_label.name)
                label_id = label['id']
            data = {
                'Title': issue.title,
                'Number': issue.number,
                'Assignees': ', '.join([a.login for a in issue.assignees]),
                'Created at': str(issue.created_at),
                'Updated at': str(issue.updated_at),
                'Link': issue.html_url,
                'Label': label_id,
            }
            print(issue.title)
            existing_issue = self.find_issue_with_number(issue.number)

            if existing_issue:
                print("u %s" % (existing_issue['id']))
                self.update_issue(existing_issue['id'], data)
            else:
                print("c")
                self.create_issue(data)
        self.submit_changeset()
        self.publish_changeset()
    
    def get_issues(self):
        self.create_changeset()
        issues = self.client.data_list(
            changeset_id=self.changeset_id,
            table_id=self.issues_table,
        )
        for issue in issues:
            yield issue
    
    def get_labels(self):
        self.create_changeset()
        labels = self.client.data_list(
            changeset_id=self.changeset_id,
            table_id=self.labels_table,
        )
        for label in labels:
            yield label


def create_schema():
    c = Client("w2gJRyzNwB", base="http://127.0.0.1:8000/api")
    
    # Create Project
    result = c.project_create(
        name='Test Github Frontend Issue5',
        description='Test Github Frontend Issue5',
        is_public=True,
    )
    project_id = result['project']['slug']
    print("project id"), 
    print(project_id)

    # Create Labels Table
    result = c.table_create(
        project_id=project_id,
        name='Labels',
        description='Labels',
    )
    labels_table_id = result['table']['slug']
    print("labels table id"), 
    print(labels_table_id)
    result = c.changeset_create(project_id=project_id, summary='Create Labels Table')
    changeset_id = result['id']
    print(changeset_id)
    print(c.column_create(table_id=labels_table_id, name='Label', column_type='text', is_unique=False, changeset_id=changeset_id,))
    print(c.changeset_submit(changeset_id=changeset_id, summary='Create Issue Table'))
    print(c.changeset_publish(changeset_id=changeset_id))

    # Create Issues Table
    result = c.table_create(
        project_id=project_id,
        name='Issues',
        description='Issues',
    )
    issues_table_id = result['table']['slug']
    print("issues table id"), 
    print(issues_table_id)
    result = c.changeset_create(project_id=project_id, summary='Create Issue Table')
    changeset_id = result['id']
    print(changeset_id)
    print(c.column_create(table_id=issues_table_id, name='Title', column_type='text', is_unique=False, changeset_id=changeset_id,))
    print(c.column_create(table_id=issues_table_id, name='Number', column_type='number', is_unique=False, changeset_id=changeset_id,))
    print(c.column_create(table_id=issues_table_id, name='Assignes', column_type='text', is_unique=False, changeset_id=changeset_id,))
    print(c.column_create(table_id=issues_table_id, name='Created at', column_type='text', is_unique=False, changeset_id=changeset_id,))
    print(c.column_create(table_id=issues_table_id, name='Updated at', column_type='text', is_unique=False, changeset_id=changeset_id,))
    print(c.column_create(table_id=issues_table_id, name='Link', column_type='text', is_unique=False, changeset_id=changeset_id,))
    print(c.column_create(table_id=issues_table_id, name='Label', column_type='foreign_key', is_unique=False, changeset_id=changeset_id, target_table=labels_table_id))
    print(c.changeset_submit(changeset_id=changeset_id, summary='Create Issue Table'))
    print(c.changeset_publish(changeset_id=changeset_id))


if __name__ == "__main__":
    # create_schema()
    loader = GithubLoader()
    # loader.load()
    issues = loader.get_issues()
    for issue in issues:
        print(issue)

    labels = loader.get_labels()
    for label in labels:
        print(label)
