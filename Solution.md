# Solution

## Part 1

### Setup (requirement 1)
I cloned the original project and created my own empty repository (I didn't fork it).
I renamed the original remote to `upstream` and added my repository as `origin`.
This way I push only to my repo, but I still have a link to the original project.

I added akritiko-york as a collaborator and turned off Actions and Dependabot in the settings.
After the first push Dependabot still opened pull requests. I found out that the
updates come from the file `.github/dependabot.yml`, so turning it off in the
settings was not enough. I deleted the file on master and closed the pull requests.

### Requirement 6 – dead end
After step 3 (editing on GitHub) and step 4 (editing on my computer), develop had
one new commit on GitHub and a different new commit on my laptop.
When I tried to push, GitKraken showed that my develop is behind origin/develop
and the push was rejected. If Git accepted it, the commit from GitHub would be lost.

To fix it I used Pull. Both commits had replaced the same line (`pass`) in
`app/core/user.py`, so I got a merge conflict. The first time I aborted the merge,
because I thought it was an error. The second time I opened the file in VS Code,
chose "Accept Both Changes", put the username line first and finished the merge.
After that the push worked. I didn't use Force Push, because it would delete the
commit from GitHub.

How I could have avoided it:
- pull before I start working
- not edit the same branch on GitHub and on my computer at the same time
- make changes on a feature branch and merge them with a pull request

### Other notes
- In step 11 I merged feature/step-2 into develop with `--no-ff`. I wanted a merge
  commit, so it's visible in the history where the feature was added.
  Then I merged develop into feature/step-1 so it has the newest code.
- `main_runner.py` was only on feature/step-1, so I created feature/step-3 from
  feature/step-1 and feature/step-4 from feature/step-3. That's why the later
  pull requests also show the older commits.

### Requirement 19 – bad commit message
The message "Some changes" doesn't tell what was changed or why.
In the history it's useless, you have to open the commit to understand it.

I didn't use `git commit --amend`, because the commit was already pushed.
Changing it would need a force push, and that rewrites the history on GitHub.
So I did what I wrote in my review: I made a new branch `feature/add-second-user`
from feature/step-3, added the Avery lines again and committed them with the
message "Add second example user to main_runner". Then I opened a new pull request
(#18) and closed the old one (#17) with a comment that links to the new one.

The collaborator invitation was pending for a while, so I could add the reviewer
on #16 only after it was accepted. I did this before merging #18.
Because #18 also had the feature/step-3 commits, GitHub marked #16 as merged
automatically after I merged #18.

### Requirement 21 – release 1.0.0
In Gitflow the code goes to master only through a release branch (or a hotfix).
I made `release/1.0.0` from develop and changed the version in `pyproject.toml`
from 0.0.0 to 1.0.0. I merged the release branch into master with `--no-ff`,
added the tag `v1.0.0`, and merged it back into develop, so develop also has
the new version number. At the end I published the GitHub release v1.0.0,
so the customers can download this version.

It's 1.0.0 because it's the first version for the customers.

### Requirement 22 – new requirement
`__str__` is a new feature, so I used a feature branch `feature/user-str-method`
from develop. It's not a hotfix, because it doesn't fix a bug in production.
It also can't go in a release branch, because release branches don't get new features.
I stopped working on it when the bug came (requirement 23). After the hotfix
I finished it and merged it into develop with a pull request.

### Requirement 23 – hotfix 1.0.1
The bug (`usrname` instead of `username`) was in the code the customers already had,
so it had to be fixed fast, without waiting for the new feature.
That's why I used a hotfix branch, `hotfix/1.0.1` from master.
I fixed the line and changed the version to 1.0.1. Then I merged the hotfix into
master, added the tag `v1.0.1`, and merged it into develop too, so the bug doesn't
come back in the next release. I also published the GitHub release v1.0.1.

It's 1.0.1 because it's only a bug fix, so only the last number goes up.