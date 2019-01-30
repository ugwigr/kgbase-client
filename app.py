from github import Github
from sets import Set
from client import Client
import time

IS_PROD = False

class GithubLoader(object):
    def __init__(self):
        self.github = Github("e65a450c670366efa4811ff55c7d96bf89bcf19e")
        self.repo = self.github.get_repo("thinknum/thinknum_base")

        if IS_PROD:
            self.client = Client("20g6qla0yb15qzjz")
            self.issues_table = "frontend-issues-LXPEI2mxjV6cI2nGGcn"
        else:
            self.client = Client("ekoknrzv45k38qeh", base="http://127.0.0.1:8000/api")
            self.project = "github-LVjeOIJl4LOxN2DK0f1"
            self.issues_table = "frontend-issues-LXNjNZ39V5E5-QhCal7"
            self.labels_table = "labels-LXTJd70_Vo1fime-mWD"

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
        self.changeset_id = self.client.changeset_create(project_id=self.project, summary="Loading frontend issues from GitHub")
        print("Created changeset with ID: %s" % (self.changeset_id,))

    def submit_changeset(self):
        self.client.changeset_submit(self.changeset_id)

    # Labels

    def find_or_create_label(self, name):
        label = self.find_label_named(name)

        if not label:
            label = self.create_label(name)

        return label


    def find_label_named(self, name):
        labels = self.client.data_list(
            self.changeset_id,
            self.labels_table,
            filters={'Label': name}
        )
        return next(iter(labels), None)

    def create_label(self, name):
        label = self.client.data_create(self.changeset_id, self.labels_table, {
            'Label': name,
        })

        return label

    # Issues

    def create_issue(self, data):
        self.client.data_create(self.changeset_id, self.issues_table, data)


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

            self.create_issue({
                'Title': issue.title,
                'Number': issue.number,
                'Assignees': ', '.join([a.login for a in issue.assignees]),
                'Created at': str(issue.created_at),
                'Updated at': str(issue.updated_at),
                'Link': issue.html_url,
                'Label': label_id,
            })

        self.submit_changeset()

loader = GithubLoader()
loader.load()
