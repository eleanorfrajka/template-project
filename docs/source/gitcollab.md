Collaborate with git
====================

See also, the description of actions in https://github.com/eleanorfrajka/template-project/pull/1.

The instructions below assume that you have cloned this repository, renamed the `projectName` to a project of your own, and would like to work on it - potentially with other people.

### Forking an existing repository

Suppose the original repository is located at: `https://github.com/ifmeo-hamburg/projectName`, and you would like to contribute to it.

When you first work with a shared repository, you will want to:

#### 1. Fork a repository

**Github.com**: Fork the repository into your own Github account.  If prompted, specify that you would like to contribute to the original project.  

#### 2. Clone to your computer

**Github.com**: From your forked repository, clone the repository to your computer.  

(i) Navigate to your repositories on GitHub, `https://github.com/YourGitHubUsername/projectName`.  Click the green `<> Code` dropdown button, and choose a method to clone this.  If you're not familiar with cloning repositories to your computer, choose `Open with Github Desktop` which will require you to have the application "GitHub Desktop" on your computer.  

(ii) When prompted, choose where on your computer you would like this to live (`/a/path/on/your/computer/`).  

**Tip:** IF you use a cloud backup service, you may find it is recommended to *not* put this in a folder that is synced with the cloud. This is because the online backups via a cloud service will need to keep copying files back and forth when you switch branches (which replaces the files in your active directory with the versions from each branch), and depending on timing, the synchronisation could cause errors or duplication.  Additionally, using git negates much of the need for cloud backups as local commits *and* pushes to the online git repository provides backups by design.

#### 3. Find the clone on your computer

**Your computer** in File Explorer (Windows) or Finder (Mac): Now you have a copy of the repository on your computer, with the associated "git" tracking information.  The repository already knows the history of changes, and has the necessary structure to update.  These are in a hidden folder within the repository folder (likely called `/a/path/on/your/computer/projectName/.git`).   This is a "main" branch of your forked repository `https://github.com/YourGitHubUsername/projectName`.  The "upstream" is where the project originated.  In this example, `https://github.com/ifmeo-hamburg/projectName`.

#### 4. Create a branch for edits

**Your computer** in a terminal window: When you'd like to start making changes in your repository, **first** make a new branch. For a forked repository from someone else's original repository, you will never work in your "main" branch.  

To make a branch, at the command line, the series of steps would be (from within `/a/path/on/your/computer/projectName/`):
```
$ git checkout main
$ git pull
$ git checkout -b yourname-patch-1
```
where you change "yourname" to your first name (or other useful identifier, e.g. your GitHub username).

This branch will now be up-to-date with the latest changes within `main` (which is what the `git pull` command does), but will have a separate copy for you to make your edits in.

**Suggested naming convention:** `yourfirstname-patch-#` where `#` increments by one for each new branch you make.  Some people also name branches by the topic or issue that branch is addressing.  So far, I've found for early code development that I'll intend a branch for one purpose, but find another that should be fixed/changed first, and then I have a branch name called `eleanor-docs-1` but it's really about a new test of plotters (or something).

#### 5. Make an edit in the branch

**Your computer** in VS Code (or wherever you work on Python): Make a change to a file.  Even adding an extra line of whitespace will do this.  Then save the file.

#### 6. Commit the change in your branch

In VS Code, to commit the change, you will navigate to the "source explorer" in the left hand bar, and add a commit message (text box above the blue "Commit" button).  This should be short, explaining in present tense what the commit does.

Optional (recommended): Add a short code at the beginning of the commit message (one word) to help categorise what the commit is doing.  See (https://dev.to/ashishxcode/mastering-the-art-of-writing-effective-github-commit-messages-5d2p).  Options include things like:

    - "feat: <extra text explaining more detail>" when you're adding a new feature or functionality
    - "fix: <extra text explaining more detail>" when you're committing a fix for a specific problem or issue
    - "style:" - when you're making changes to style or formatting but not functionality (user should experience no change)
    - "refactor:" - changes to the code that improve structure or organisation, but don't add features or fix bugs
    - "test:" - when you're adding or updating tests for the code
    - "chore:" - updating changes to the build process or other tasks not directly related to the code (e.g., GitHub workflows)
    - "perf:" - Changes to improve code performance, e.g. speed
    - "ci:" - changes to the continuous integration process

#### 7. Create a pull request to origin

**Your computer** in VS Code: Sync the commit to main.  If this is the first time you've done this from your branch, you will need to set the upstream.  Set the upstream to be `https://github.com/ifmeo-hamburg/projectName`.  This will direct the pull request to the original main repository (not your main).  Exception, if you're working on a fork where the original main repository lives in your GitHub account `https://github.com/yourGitHubUsername/projectName` then it will be pulled to your main.  

#### 8. Compare pull request on GitHub.com

**Github.com**: Navigate to the original repository `https://github.com/ifmeo-hamburg/projectName` and you should see the pull request has come through.  There will be a shaded bar at the top with a button "compare and pull request".  Click this button and on the next page add some useful details for the rest of the contributors to understand what your commit is doing.  

Note that the default version of this template includes some tests to be run when you submit a pull request.  The python code for these tests is located in `tests/`.  The Github Actions "workflow" that calls the tests is in `.github/workflows/tests.yml`.  It requires that your `requirements-txt` file includes the package:
```
pytest
```

If you're using the `micromamba` version (commented out below in the `tests.yml` file, then you'll additionally need the package
```
pytest-cov
```
in `requirements-dev.txt`.

### Collaborating with others on your repository

The steps are as above, but your main repository is the original main repository.  