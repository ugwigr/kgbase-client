from github import Github
from sets import Set

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

print "All issues: %s" % (all_issues,)


