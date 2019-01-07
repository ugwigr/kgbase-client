from github import Github
from sets import Set
from client import Client

g = Github("e65a450c670366efa4811ff55c7d96bf89bcf19e")

repo = g.get_repo("thinknum/thinknum_base")

print "Repo name: %s" % (repo.name,)

def find_issues(user):
    label_high_priority = repo.get_label("Priority: High")
    issues = repo.get_issues(state="open", assignee=user, labels=[label_high_priority])
    return [issue for issue in issues]

all_issues = {}

for user in ["vojto", "lprokein"]:
    issues = find_issues(user)
    for issue in issues:
        all_issues[issue.number] = issue

all_issues = all_issues.values()

print "Total issues count: %s" % (len(all_issues),)

# Copy into Metabase

client = Client("ttsejo1uh45dvf0n")
table_id = "frontend-issues-LVe7zDLnraMRnJTljhR"

changeset_id = client.create_changeset(table_id, "loading issues")

for issue in all_issues:
    client.create_data(table_id, changeset_id, {
        'title': issue.title,
        'number': issue.number,
    })

client.submit_changeset(table_id, changeset_id, "loaded issues")
