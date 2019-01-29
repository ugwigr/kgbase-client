from github import Github
from sets import Set
from client import Client

class GithubLoader(object):
    def __init__(self):
        self.github = Github("e65a450c670366efa4811ff55c7d96bf89bcf19e")
        self.repo = self.github.get_repo("thinknum/thinknum_base")

        self.client = Client("ekoknrzv45k38qeh", base="http://127.0.0.1:8000/api")

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

    def load(self):
        issues = self.find_frontend_issues()

        print "Total issues count: %s" % (len(issues),)

        # Copy into Metabase

        project_id = "github-LVjeOIJl4LOxN2DK0f1"
        table_id = "frontend-issues-LXNjNZ39V5E5-QhCal7"

        changeset_id = self.client.changeset_create(table_id, summary="Loading frontend issues from GitHub")

        print("Created changeset with ID: %s" % (changeset_id,))

        for issue in issues:
            # First, let's try to find an existing record
            records = self.client.data_list(table_id, filters={
                'Number': issue.number,
            })

            print("Existing records: %s" % (records,))

            self.client.data_create(table_id, changeset_id, {
                'Title': issue.title,
                'Number': issue.number,
                'Assignees': ', '.join([a.login for a in issue.assignees]),
                'Created at': str(issue.created_at),
                'Updated at': str(issue.updated_at),
                'Link': issue.url,
            })

        self.client.changeset_submit(table_id, changeset_id)

loader = GithubLoader()
loader.load()
